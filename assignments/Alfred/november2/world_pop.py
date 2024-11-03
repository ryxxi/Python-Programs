year = 1
pop_now = 8186082500
current_pop = pop_now
estimated_pop = round(current_pop * 1.1)
pop_increase = estimated_pop - current_pop
double_year = 0
quad_year = 0

print(f"{'Years since 2024'} {'Estimated population': >40} {'Population increase': >40}")

for year in range (1, 101):

	print(f"{year} {estimated_pop: >51} {pop_increase: >39}")
	current_pop = estimated_pop
	estimated_pop = round(estimated_pop * 1.1)
	pop_increase = estimated_pop - current_pop

	while (estimated_pop >= pop_now * 2):

		double_year = year
		break

	while (estimated_pop >= pop_now * 4):

		quad_year = year
		break

print(f"The current population will have doubled in 2032")
print(f"The current population will have quadrupled in 2040")