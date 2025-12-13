# Information Security
# Homework 4

Fabián Andrez De La Cruz
Roberth Lara

## 1. Foundational Research: Ecuadorian Data Sovereignty (LOPDP)

Ecuador's Ley Orgánica de Protección de Datos Personales (LOPDP), enforced starting in July 2023 , establishes comprehensive individual rights over personal data. This module requires you to research the specific mandates of this law as they relate to automated decision-making and cross-border data management.   

### What are the three core principles (criterios mínimos) that govern all data processing activities under the LOPDP?

Perhaps I have misread the LOPDP, but I have found way more than 3 core principles. I will list the ones I consider the most relevant.

* Finalidad 

Data can only be used for specific, clear, and legitimate purposes that were told to the person. It cannot be used for a different purpose.

* Pertinencia y Minimización

Only the data that is strictly necessary for the stated purpose may be collected and used.

* Transparencia

People must clearly understand how and why their data is being used. Information must be simple and accessible.


### Locate the specific article (or section within an article) of the LOPDP that grants the data subject the right “to not be object of a decision based solely on automated valuations”. Explain the details and protections it provides.  


This right is found in Article 20 - 'Derecho a no ser objeto de una decisión basada única o parcialmente en valoraciones automatizadas '


If a decision is automated (for example made by an AI), the person has the right to:

* Ask for an explanation of how the decision was made

* Give comments or objections

* Request the criteria used by the automated system

* Know what data was used and from where

* Challenge or dispute the decision

The law also says that automated decisions cannot be forced through contract, and the person must be informed of this right at the first communication of such a decision.

### In the context of an AI-driven system (e.g., hiring or loan approval), explain the operational impact of this right. How does this LOPDP provision compel a data controller to provide human intervention or oversight?   


Under Article 20, an AI cannot be the only decision-maker if the decision affects important rightsx.

In simple terms, the company must have a human review the AI's decision, the company must be able to explain why the AI rejected or approved a person, and the person must be allowed to contest the decision and ask for a human to reconsider it.

### Under what conditions is the international transfer of personal data restricted by the LOPDP?   

International transfers are covered mainly in Articles 33–36.

The law restricts international transfer when:

* There is no valid legal basis for the transfer (consent, contract, law, etc.).

* The recipient country does not provide adequate protection comparable to Ecuador.

* The transfer does not follow the principles (like purpose, minimization, confidentiality).

* The transfer is not clearly informed to the data subject 
.

If none of the exceptions of Article 36 apply, the transfer cannot be done without consent or another valid legal basis.

### Explain the role of the Data Protection Authority (DPA) regarding international data transfers. How does this requirement create operational friction or regulatory compliance barriers for a multinational AI company that typically relies on centralized cloud infrastructure outside of Ecuador?   

The DPA makes sure Ecuadorian data is not sent abroad without strong protections, which can slow down or complicate how global AI companies operate.


## 2. Corporate Policy Scrutiny: The Data Repurposing Conflict

Major generative AI companies frequently face scrutiny for collecting and repurposing user data (such as chat inputs) for model training, a practice that directly challenges the principles of purpose limitation and explicit consent in global privacy laws.   

### Select two major generative AI providers (e.g., OpenAI, Meta, or Anthropic). Briefly summarize how each company differentiates the data usage practices between their Enterprise/API Services (for paying business clients) and their Consumer/Chatbot Services (for free public users) regarding model training.   



Provider A: OpenAI

* Enterprise/API customers

    * OpenAI does not use API or Enterprise customer data for training by default.

    * Companies using the API keep control of their data.

* Consumer ChatGPT (free or personal accounts)

    * Chat messages may be used to improve OpenAI models unless the user opts out.

Provider B: Meta (LLaMA + Meta AI)

* Enterprise/API style uses

    * Meta's business integrations do not use company data to train public models.

* Consumer Meta AI (Instagram, WhatsApp, Facebook)

    * Public interactions, posts, and messages to Meta AI can be used for training unless a person uses the opt-out form.

### Analyze the public-facing policy for the consumer chat version of one of your selected companies. Identify the type of user input data (e.g., chat content, account info, technical data) that may be used for model training.   

According to OpenAI's consumer policy:

* User data that may be used for training:

* Chat content (messages the consumer writes)

* Uploaded files or images

* Account information (email, profile settings)

* Technical data (device info, IP, usage logs)

This applies only to the consumer version, not to API/Enterprise customers.


### Describe the practical process a user must follow to opt out of having their data used for training (e.g., submission of a form, navigation of settings, or use of a specific toggle).  

For ChatGPT the process is as follows: 

1. Go to Settings in ChatGPT.

2. Open Data Controls.

3. Turn off “Improve the model for everyone”

After opting out, new conversations are not used for training. Some other platforms require a form to be submitted in order to opt out.

### Critically evaluate: How does this opt-out mechanism conflict with the LOPDP’s mandate for prior, informed, and explicit consent for data processing?   

The LOPDP wants “ask first” while many AI companies do “use first, let the user turn it off later”.

### Legal Risk Scenarios: Research a recent legal challenge or public controversy where an AI company (e.g., Meta, LinkedIn, or Amazon) was accused of using previously collected user-generated content or biometric data for a new, secondary AI training purpose without proper consent. Briefly summarize the nature of the alleged violation (e.g., biometric privacy, repurposing of communication data).   


In 2024, Meta faced significant backlash after announcing plans to use users public posts, captions, and photos from Facebook and Instagram to train its new Meta AI models. Critics argued that Meta was repurposing content that had originally been shared for social networking, not for artificial intelligence development, violating basic privacy principles such as purpose limitation and the requirement for explicit consent. Privacy groups in Europe also warned that photos and other content could reveal sensitive or even biometric data, which cannot be reused for new purposes without clear authorization. Due to these concerns, regulators in the EU intervened and forced Meta to pause parts of its AI training program. At the core of the controversy were allegations that Meta treated old user generated content as automatically available for AI training, even though users had never been asked whether they agreed to this new use.



## 3. Technical Risk Assessment and Mitigation

AI systems, especially those processing sensitive data, require robust security and governance to prevent privacy harms and data access risks. This module focuses on threat modeling and risk management.

### Choose one high-risk application and detail a specific scenario where it could lead to severe harm or unauthorized data access

Application: AI system that analyzes medical images to predict cancer risk.

Scenario of harm:
If the model is trained on improperly protected patient data and the system is hacked, attackers could access thousands of people's medical records, exposing diagnoses, and other sensitive details. This could cause emotional distress, discrimination (insurance denial), and long-term privacy harm. 

### Assume we deploy a new AI-driven predictive policing system deployed in a major Latin American city. Describe how historical bias present in the training data (e.g., police reporting practices)  could cause the system to disproportionately target and surveil marginalized communities , resulting in discriminatory legal effects (a violation of LOPDP’s principle of proportionality  and the right to object to automated decisions ).   


The AI will simply repeat and amplify those patterns. It may mark the same communities as “high-risk zones” even if crime rates are not actually higher, causing heavier surveillance, more stops, and more arrests. This creates a discriminatory legal effect because people from these groups are treated unfairly by an automated system. Under the LOPDP, this violates the principle of 'proporcionalidad' and the right to not be subject to an automated decision, since the system's decisions directly affect people without proper human review.

### Explain the security threat known as "Model Memorization" or "Data Leakage" in generative AI. If an AI chatbot (used internally by a hospital) accidentally memorizes and reveals unmasked patient health information (PHI) shared during a training prompt, what specific privacy right under the LOPDP would be violated?   


Model memorization occurs when a generative AI system accidentally remembers and repeats sensitive information from its training data. If a hospital chatbot memorizes and later reveals patient health information (PHI), this is a data leakage event.

Which LOPDP right is violated:
Revealing private health data violates the patient's right to confidentiality and protection of sensible data, and specifically their right to not have their data used for a purpose they did not consent to. It also violates the right to the security of personal data and the principle of minimization, because the system should never expose or reuse health information in outputs.