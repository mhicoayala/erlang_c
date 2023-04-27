from erlang import get_erlang_c

volume = 200
aht = 180 # seconds; 3 mins
traffic_intensity = (volume * 3) / 60 # 10
target_answer_time = 20 # seconds
target_sla = .80 # industry standard is 80
shrinkage = 0.30 # industry standard is 80 as well

results = get_erlang_c(
    volume = volume,
    traffic_intesity = traffic_intensity,
    target_answer_time = target_answer_time,
    aht_seconds = aht,
    target_sla = target_sla,
    shrinkage = shrinkage
)

for i in results:
    print(f'{i}: {results[i]}')


