# Khantil_Desai_MachineLearning_Prepr

The first half of the challenge revolves around visualization of labour data on StatsCan for which I created pivot tables and charts to display the effects of demographic factors like age, sex, background, and education level on employment.
The second half of the challenge revolves around determining how skills relate to various jobs.

For this, the job skills csv was parsed and the count of "key words" in the preferred requirements was used as a proxy for how important that skill is for that specific work. This was accomplished by measuring the frequency of non-trivial words in the preferred skills for the various job types. I.e. the words in the preferred qualifications column was mapped to the job category column. For example, for Hardware Engineering roles, the most important factor was having an engineering degree or Science Degree, followed by knowledge of Manufacturing and Design.

The program I wrote generates pie charts for every type of role in the company. These pie charts can be interpreted as how important certain skills are for that specific job type. For example, in marketing and communications, having a BA or BS is the most import factor as they account for 75% of the total decision.

To better this model, a General Adversarial Neural Network (GAN) can be developed. Although simpler MLP (Multilayer Perceptron) neural networks can be used to improve the accuracy of the model, a GAN could reach much higher levels of accuracy. 
Refer to:https://venturebeat.com/2019/12/26/gan-generative-adversarial-network-explainer-ai-machine-learning/

To implement a general adversarial network, we will essentially allow the computer to generate "fake" skills for applicants, which will be used to train the model. This will ensure that the model is not memorising what skills a certain job needs. (Which is essentially what the program is doing right now).

Ultimately, the computer will learn what skills make a good applicant based on the preferred skills in the application. This method will also allow real world data to be used more sparingly to test the network and not to train it.
