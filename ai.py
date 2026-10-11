#AI: AI is system that learns patterns from data to make predictions or generate o/p
#Ai need system performing tasks typically require human intelligence 
#Data->Pattern->ML model this process is called training process
#Prediction of new O/p based on new data after completing training process of ML model its called Inference
#Ex: Understanding sad and happy faces in images

#Neural network: F/W P   * * * Backward Propogation
#                        * * *
#      I/P Lay           * * * O/P Layer
#                          H
#                        Hidden
#Every neuron connection have weightage values which decides importance of i/p neuron to next neuron and adjust weightage values of neurons to next 
# neuron based on parameter to predict
#Feeding data to neural network, when info moves from 1st layer to another(last) it is called forward propogation and take prediction and  
# at the same time it is  done in backward direction  it is called backword propogation and take prediction and after  both propogation are done
#We adjust weight values for better prediction in this way we make neural network smarter 
#Every neuron has a additional Arbitary value which is called Bias Value 
#
#Neuron value based on formula --> f(X1w1+x2w2+x3w3+B)
#Once we have the trained network we can do Inference
#
# 



#LLM:  It's an AI trained on huge amount of data(Textual Data) to predict what word or Token comes next in sentence
#Large-->Data,Language-->Text,
#Query<-->LLM<-->Response (EVeryhting is stored)
#Its a game of probabilty of which next best word fits in response

#Tokens:    AI or LLM doesnt actually understands the Human Language like Eng,Mara,Hindi,etc
#           Every String,text is converted into No.s that is Token and process is called Tokenization
#           Ex:I--> Like--> Gener-->ative--> AI
#              [40,  1299,   4140,     1799,    20837]
#               (20 characters) (5 Tokens) 
#       
#Contex Window:  
#(user)Query(Previous Query)<-->LLM<-->Response (EVeryhting is stored)
#   Working Memory for the current conversation
#   CW is only for current active conservation
#Every conversation has a limit of tracking what happend and limit is called Context Window
#CW is Tracked in No.s of Tokens  
#EX:    gpt1-->512Tokens
#       gpt6-->1M
#       fable-->1M                             

#vectors: 
#I/P-->Tokens,TokenId-->Vectors-->LLM
#LLM doesnt understand the I/p meaning until it is converted into vectors and process is called Vectorization
#We need some weight to relate or corelate different tokens with each other
#Embeding  tells us that vector carrieas the meaning of tokens  specifically  for LLM 
#Vector is N-Daimentional array
# cat-->29-->[0.06,0.3,0.5]
#
#ML&A:  It is when we give a computer examples and let it figure out the patterns on its own 
# It comes in 3 types: Supervised learning, Un-supervised learning, Reinforcement Learning


#A:Algorithms are recipes for learning : Neural networks,decision trees,linear regression,etc 
#
#

#Attenttion:
#               
#Ex:                        I code in           python
#                                key vectors    Query vectors          
#
#when we have to understand meaning of perticular token we create a special vector called Query  vector and other tokens are called key vectors
#Math operations are performed on thses vetcors then we get attention score
#Attention tokens tells how relevent other tokens to original token


#Understanding tokens contex as compared to others tokens
#LLMs use special mechanism to do that which is called attention
#In attention mechanism we decide for a perticular individual token, is there any relevent token present and which token is impotant to understand meaning of token
#calculating attention score its called attention mechanism
#
#
#Tranformer architecture:
#  it consist of two imp blocks
#I/P-->Attention Block-->FNN(feed forward neural network)-->O/p
#In LLM the most imp work is predicting the next token so we can generate the o/p and its done by transformer architecture
#
#


#Fine-Tunning:
#   When we need a specialized LLM for specialized Domain then fine tunning is used
#LLM-->Specialized-dataset-->Fine Tunned Model
#
#
#Self-supervised learning:
#                           Data
#                       labeled     unlabeld
#ex:  when theres a data, LLM hides some data and then try to predict the hiden data with help of  non hiden data
##
#Reinforcement learning::
#When model behaves as intended to predict next token then we reward(+ value) the model and if it doesnt then we give it penalty(-value)
#The model in reinforement learning is called agent
#Agents work is to maximize the rewards 
#the role of agent is to maximize the rewards
#Reinforcement learning work on human feedback
#Eevry organization(LLM) need responses like human should  prefer


#RAG Retrieval augmented Generation::
#some times our LLM doesnt have access to companies data
#when LLM get access(form of graph,sql,vector database) from different database then process it to generate better 
# response is called RAG
#RAG  Pipeline:the data we want to give access to LLM to retrive to generate a better response and this is called RAG Architecture 
# and not to make public   
#We dont give entire access of database to LLM so that security is maintained 
#RAG pipeline doesnt access the entire database instead it access small vectors chunks of data
#It can only access relevent chunks of query so that theres high level of data privacy

#Vector Databse::
#   vector databse is different from other databse because it have ability to perform semmantic
# search(meaning based search)
#Documents -->chunks-->Vector embeddigns-->vectors database



#Few-Short prompting::
#this is prompting process which can improve qualtiy of reponses
#Its meaning is we give few examples.
#prompt(few relevent examples) -->LLM --> Response
#LLM will find patterns based on examples to suggest more responses
#
#
#
#Model context Protocol::
#MCP is protocol which defines how  any model gets additional external context.
#Query-->MCP Client<-->LLM-->Response
#           |
#          MCP server for Github

#Context Engineering::
#The process of designing and managing this addtional context this addtional infromation which passed on to LLM along with Query is called context Engineering.
#

#Multi-modal Model::
#       These are models which are capable of proccesing different form of data
#       it can process or genrate text data
#       can understand or generate images
#       also work on videos,audio,etc.
#       
#Ai Agent::
#       When we need to perform some actions like emailing,making shcedual then we need to use Ai Agent
#       ai agents are systems which we give some task to perform also ai agents have access to tools,resources 
#       on that basis we execute some tasks
#               LLM(Brain)             
#               |
#       task-->system-->execute tasks
#               |
#               Tools,resources
#       Brain behind operation of  the ai agents is LLM 
#       Behind the scences logic ,reasoning is done by LLMs.
#       System around LLM is callled Ai Agent.
#
#Chain of Thoughts::
#           We have 2 cases:1.:Query(based on query)-->LLM-->Direct ans
#                           2.:Query-->LLM-->Thinking process(reasoning process)(Multiple steps breakdown)
#           When we give Query to LLM then it shows us thinking process,reasoning peocess then how LLM breakdown
#           query in multiple steps  to generate O/P. is called Chain of thoughts

#Reasoning Model::
#               Types of Reasoning:
#                  1.Chain of thoughts
#                   2.Tree of thoughts:Model do reasoning in tree format
#                   3.Graph of thoughts


#Small language Model::
#               it consist of small num. of parameters thats why it s called small language model
#               less than 10B parameters
#               cheaper and they provide a higher level of privacy as compared to genral LLMs
#

#Distillation::
#           Its a way of training the small language model(SLM)
#           We take LLM which becomes Teacher for SLM.
#           We provide same I/P to LLM and SLM then SLM need to predict the O/p of LLM
#           In this way SLM try to mimic the reasoning of LLMs O/p
#           I/P-->LLM-->O/P
#             |          |
#           I/P-->SLM-->O/p
#
#Quantization::
#           Types of Q.:1.Post training Quantization:We train the model normally after the training we do Quantization and Inference cost goes down
#                       2.Quantiztion aware training:we simulate the low precision training behaviour in LLM during training process itself