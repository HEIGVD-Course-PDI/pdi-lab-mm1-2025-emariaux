Questions to answer
==================================

These are the questions related to the M/M/1 queueing model using SimPy.

You will need to answer the questions in this file. Your answers will be graded. 

You can answer in English or French.


1-Implement the M/M/1 queueing model in SimPy
---------------------------------------------

### The implementation in the file `models/simpy_m_m_1.py` counts for 4 points maximum. (4p)


2-Validate the simulation model
-------------------------------

#### Show at least 3 different simulation results with different parameters and compare them with the analytical model. (6p)

| | $\lambda$ | $\mu$ | E[T] Theory | E[N] Theory |  E[T] Sim | E[N] Sim |
|--|----|---|---|---|--|--|
|1.| 10 client/s | 50 clients/s | 0.0250s | 0.25 | 0.0250s | 0.2523 |
|1.| 20 client/s | 50 clients/s | 0.0333s | 0.667 | 0.0335s | 0.6909 |
|1.| 10 client/s | 100 clients/s | 0.0111s | 0.111 | 0.0111s | 0.1104 |

*The simulation is accurate with the analytical model.*

3-Evaluate the impact of an load increase
-----------------------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 30/s` and `SERVICE_RATE = 50/s`? (2p)

*Mean response time: 0.0504 seconds ; 
Mean number of clients in the system: 1.5101*

#### What are the simulation results when running with a 40% increased `ARRIVAL_RATE`? (2p)

*With an `ARRIVAL_RATE = 42/s`.*

*Mean response time: 0.1235 seconds
Mean number of clients in the system: 5.1667*

#### Interpret and explain the results. (3p)

*With a 40% increase in the arrival rate, the mean number of clients E[N] is 4 times higher. Moreover, the mean response time E[T] is more than 2 times higher.*

*Therefore, when we increase the arrival rate by 40%, we do not observe a proportional 40% increase in response time and mean number of clients. The increase is much more significant.*


4-Doubling the arrival rate
---------------------------

#### What are the simulation results when running with `ARRIVAL_RATE = 40/s` and `SERVICE_RATE = 50/s`? What is the utilization of the server? (2p)

*Mean response time: 0.1027 seconds
Mean number of clients in the system: 4.1301*

*The utilization if the server is 40/50 = 0.8. So the server is used 80% of the time.*

#### What is the value of `SERVICE_RATE` that achieves the same mean response time when doubling the `ARRIVAL_RATE` to `80/s`? What is the server utilization in that case? (2p)

*Mean response time: 0.0499 seconds
Mean number of clients in the system: 3.9665*

*With `SERVICE_RATE = 100/s` we had the same 80% of utilization*

#### Use the analytical M/M/1 model to confirm your findings. (3p)

*With the analytical model the utilization is $\rho = \frac{\lambda}{\mu}$. 
In the first case: $\rho = \frac{40}{50} = 0.8$. 
In the second case with doubled arrival rate: $\rho = \frac{80}{100} = 0.8$. 
Both configurations maintain the same utilization of 80%*

#### Describe and interpret the results. (3p)

*The results demonstrate an important property of M/M/1 queues: when we double both the arrival rate 
$\lambda$ and the service rate $\mu$ while maintaining the same utilization $\rho$, 
the mean response time E[T] remains constant.*

*In our experiments:*
- *Configuration 1: λ=40/s, μ=50/s → E[T]≈0.10s*
- *Configuration 2: λ=80/s, μ=100/s → E[T]≈0.05s*

*However, the mean number of clients E[N] doubles from approximately 4 to 8. 
This confirms Little's Law: E[N] = $\lambda$ × E[T]. When $\lambda$ doubles and E[T] stays constant, E[N] must double.*

*This scaling property is crucial for system design: to handle twice the traffic while 
maintaining the same response time, we need to double the service capacity ($\mu$). 
The system will then process twice as many clients with the same individual delay, 
but the queue will contain twice as many clients on average.*


5-Rule of Bertsekas and Gallager
--------------------------------

#### Describe your experiments and results. (2p)

> *"A transmission line k times as fast will accommodate k times as many packets at k times smaller average delay per packet."*

*First we have `ARRIVAL_RATE = 10/s` and `SERVICE_RATE = 50/s`. The results :*

*Mean response time: 0.0251 seconds \
Mean number of clients in the system: 0.2478*

*We use k = 2*
*So if we double the transmission line, so `SERVICE_RATE = 100/s`, we have the following results :*

*Mean response time: 0.0112 seconds \
Mean number of clients in the system: 0.1125*

*When we double the service rate E[T] was divide by two and E[N] too.
So if we want to have the same number of clients whe need to double the Arrival time.
So `ARRIVAL_RATE = 20/s`*

*Mean response time: 0.0125 seconds \
Mean number of clients in the system: 0.2468*

*We have divide by k the Mean response time E[T] and the same mean number of clients in the system E[N].*
*Whith these 3 simulations we can confirm the rule of Bertsekas and Gallager*


#### Provide an analytical explanation of your findings. (2p)

*For an analytical explanation, consider the first simulation where $\lambda = 10$ and $\mu = 50$.*

*The mean response time is calculated as $E[T] = \frac{1}{\mu - \lambda}$ 
and the mean number of clients as $E[N] = \frac{\rho}{1 - \rho}$, where $\rho = \frac{\lambda}{\mu}$.*

*For E[N]: if we multiply both $\mu$ and $\lambda$ by k, we maintain the same 
$\rho$ since $\rho = \frac{k\lambda}{k\mu} = \frac{\lambda}{\mu}$. Therefore, E[N] remains constant.*

*For E[T]: we get a result k times smaller because 
$E[T] = \frac{1}{k\mu - k\lambda} = \frac{1}{k(\mu - \lambda)} = \frac{1}{\mu - \lambda} \cdot \frac{1}{k}$.*

*Therefore, E[T] is multiplied by $\frac{1}{k}$, meaning it is divided by k.*


Conclusion
----------

#### Document your conclusions here. What did you learn in this lab? (2p)

*This lab provided valuable insights into the behavior of M/M/1 queueing systems through both simulation and analytical analysis.*

*1. A modest in arrival rate (40%) can cause a disproportionate increase in response time (2x) and queue length (4x). 
This demonstrates that queueing systems exhibit highly non-linear behavior as utilization increases, 
particularly when approaching saturation.*

*2. When both arrival rate λ and service rate μ are scaled by the same factor 
k while maintaining constant utilization ρ, the mean response time E[T] remains constant, 
but the mean number of clients E[N] scales proportionally with k. This is the Bertsekas and Gallager rule, 
which is crucial for capacity planning.*

*3. The SimPy simulation results closely matched the theoretical M/M/1 formulas,
confirming both the accuracy of our implementation and the validity of the analytical model for predicting system behavior.*
