# Dynamic-Truck-project
This is my first project using Python on dynamic programming. My friend Liangliang Xu mentors and gives me lots of help. 
The purpose of this project is to provide a framework to apply dynamic programming to help the driver to schedule the rest
stops to mitigate the risk on the road given the weather and traffic conditions. According to our review, the major factors 
which have a significant impact on the risk are related to the weather and traffic. As we know, when building a model based
on the MDP, the less number of states and actions will decrease the computational time. However, the factors fromthese two
areas selected as inputs in risk statistical model are different in each paper. Also, the interaction between these can't be 
ignored. To reduce the complexity in MDP, we assume that the external driving condition could be integrated into one indicator. 
Besides that, the internal factor under consideration in our model is related to the driver's fatigue referred to as "g" in our 
code. Later, researchers could fill in the presumable parameters in our model. Furthermore, by utilizing the internal condition, it 
gave us a chance to compare the autonomous vehicle with the human related vehicle. The big difference between these types of
driving is that there is no internal effect for the non-human driving if we assume the autonomous vehicle can make the same 
decision like human such as changing the lane, avoiding obstacles, etc..The comparison between two types of driving could be 
presented by playing with the initial drving performance(g0).

