from math import factorial, e, ceil

# Probability of Waiting
def prob_waiting(traffic_intesity, num_agents):
    x = ((traffic_intesity ** num_agents) / factorial(round(num_agents))) * num_agents / (num_agents - traffic_intesity)
    y = 1

    for i in range(round(num_agents)):
        y += (traffic_intesity ** i) / factorial(i)

    return x / (y + x)

# Service Level
def compute_sla(pw, traffic_intesity, num_agents, targ_ans_time, aht):
    return 1 - (pw * (e ** -((num_agents - traffic_intesity) * (targ_ans_time / aht))))

# Function to calculate Erlang C outputs:
def get_erlang_c(volume, traffic_intesity, target_answer_time, aht_seconds, target_sla, shrinkage):

    # Raw Number of Agents
    raw_agent = 1
    n = round(traffic_intesity + raw_agent)

    pw = prob_waiting(traffic_intesity, n)

    act_sla = compute_sla(pw, traffic_intesity, n, target_answer_time, aht_seconds)

    while act_sla < target_sla:
        raw_agent += 1
        n = round(traffic_intesity + raw_agent)
        pw = prob_waiting(traffic_intesity, n)
        act_sla = compute_sla(pw, traffic_intesity, n, target_answer_time, aht_seconds)

    average_speed_of_answer = (pw * aht_seconds) / (n - traffic_intesity)

    percent_calls_answered_immediately = (1 - pw) * 100

    maximum_occupancy = (traffic_intesity / n) * 100

    n_shrinkage = n / (1 - shrinkage)

    return {
        'Volume': int(volume),
        'Traffic Intensity': int(traffic_intesity),
        'No. of Required Agents': int(n),
        'No. of Required Agents w/ Shrinkage': ceil(n_shrinkage),
        'Average Speed of Answer': round(average_speed_of_answer,1),
        '% of Calls Answered Immediately': round(percent_calls_answered_immediately,2),
        'Maximum Occupancy': round(maximum_occupancy,2),
        'SLA': round((act_sla * 100),2) #
    }





