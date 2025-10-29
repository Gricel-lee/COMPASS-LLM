# Mind the Prompt: Self-adaptive Generation of Task Plan Explanations via LLMs

This repository contains information and resources related to the paper "Mind the Prompt: Self-adaptive Generation of Task Plan Explanations via LLMs".

## Abstract

Integrating Large Language Models (LLMs) into complex software systems enables the generation of human-understandable explanations of opaque AI processes, such as automated task planning. However, the quality and reliability of these explanations heavily depend on effective prompt engineering. The lack of a systematic understanding of how diverse stakeholder groups formulate and refine prompts hinders the development of tools that can automate this process. We address this gap through COMPASS (COgnitive Modelling for Prompt Automated Synthesis), a self-adaptive approach that formalises prompt engineering as a cognitive and probabilistic decision-making process. COMPASS models unobservable users' latent cognitive states, such as attention and comprehension, uncertainty, and observable interaction cues as a POMDP, whose synthesised policy enables adaptive generation of explanations and prompt refinements. We evaluate COMPASS using two diverse cyber-physical system case studies to assess the adaptive explanation generation and their qualities, both quantitatively and qualitatively.

## Core Problem

Large Language Models (LLMs) can explain complex AI processes, but the quality of these explanations depends heavily on "prompt engineering"—how the request for an explanation is phrased. Different users (e.g., developers, end-users, managers) have different needs and levels of understanding, making it difficult to manually create the "perfect" prompt. This paper addresses the lack of a systematic way to automate and adapt this prompt engineering process.

## Our Solution: COMPASS

To solve this, we introduce COMPASS (COgnitive Modelling for Prompt Automated Synthesis).

COMPASS is a self-adaptive approach that treats prompt engineering as a probabilistic decision-making problem. It works by:

1 Modeling the User: It builds a model of the user's hidden ("latent") cognitive states, such as their level of attention, comprehension, and uncertainty.

2 Observing Cues: It simultaneously monitors observable interaction cues from the user.

3 Using a POMDP: This entire process is formalized as a Partially Observable Markov Decision Process (POMDP).

4 Adapting in Real-Time: The policy synthesized from the POMDP allows the system to automatically and adaptively generate better explanations and suggest prompt refinements tailored to the user's current cognitive state.

## Evaluation

We evaluated the effectiveness and quality of COMPASS's adaptive explanation generation using two different case studies involving complex cyber-physical systems in the contruction and agricultural domains. Results are available in ```/evaluation-results/```.
