import os
import json
from google import genai
from google.genai import types



class Gemini:
    def __init__(self, credential: str = "key.json"):
        self.credential = credential
        self.set_env_var()
        # Vertex AI client (uses service account)
        self.client = genai.Client(vertexai=True, project="seams26", location="us-central1")

    def set_env_var(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.credential

    def get_response(self, problem_def_path):
        # Step 1: Read local files as text
        file_paths = {
            "problemdef.txt": problem_def_path,
            "promptInstructions.txt": folder_path + "/evaluation-results/RQ1-Feasibility/llm_instructions/prompt-instructions.txt",
            "example.json": folder_path + "/evaluation-results/RQ1-Feasibility/llm_instructions/example.json"
        }

        file_contents = {}
        for name, path in file_paths.items():
            with open(path, "r", encoding="utf-8") as f:
                file_contents[name] = f.read().strip()

        # Step 2: Construct single long prompt
        prompt_text = (
            "Generate a JSON file as described in the prompt-instructions.txt.\n\n"
            f"File problemdef.txt content={file_contents['problemdef.txt']}\n\n"
            f"File promptInstructions.txt content={file_contents['promptInstructions.txt']}\n\n"
            f"File example.json content={file_contents['example.json']}"
        )

        # Step 3: Send prompt to Gemini
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[prompt_text],
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)  # disables thinking
            ),
        )

        # Step 4: Extract and save response
        output_text = response.text.strip()
        try:
            json_data = json.loads(output_text)
        except json.JSONDecodeError:
            print("⚠️ Model output is not strict JSON. Saving raw text instead.")
            json_data = {"raw_output": output_text}

        output_path = "gemini_output.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2)

        print(f"✅ Saved Gemini response to {output_path}")
        return json_data


# --- Run ---
if __name__ == "__main__":
    folder_path = "./" # Folder path
    gemini = Gemini(credential="../../../Documents/seams26-key.json") # replace with your own
    folder = folder_path + "/evaluation-results/RQ1-Feasibility/problem_def/agriculture/",
    # for file in folder
    for file in os.listdir(folder[0]):
        if file.endswith(".txt"):
            problem_def_path = os.path.join(folder[0], file)
            print(f"\n--- Processing file: {problem_def_path} ---")
                
            response = gemini.get_response(problem_def_path)
            print(json.dumps(response, indent=2))


        file_name_json = file.split(".txt")[0] + ".json"


        import json
        import re

        # Load Gemini output
        with open("gemini_output.json", "r", encoding="utf-8") as f:
            data = json.load(f)

        raw_text = data.get("raw_output", "")

        # Remove code fences ```json ... ```
        clean_text = re.sub(r"```json|```", "", raw_text).strip()

        # Sometimes the model adds extra newlines, remove them
        clean_text = clean_text.strip()

        # Parse the inner JSON
        try:
            inner_json = json.loads(clean_text)
        except json.JSONDecodeError as e:
            print("❌ Failed to parse JSON from Gemini output:", e)
            inner_json = {"error": "Failed to parse JSON", "raw_text": clean_text}

        # Save the clean JSON
        with open(file_name_json, "w", encoding="utf-8") as f:
            json.dump(inner_json, f, indent=2)

        print(f"✅ Saved cleaned JSON to {file_name_json}")
