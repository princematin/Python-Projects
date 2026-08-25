# Importing Person classes
from person import Person
from engineer import Engineer
from teacher import Teacher
from worker import Worker

# Importing WorkPlace classes
from work_place import WorkPlace, WorkPlaceIsFull, Consts as WorkPlaceConsts
from mine import Mine
from school import School
from company import Company

# Creating an engineer
raha = Engineer(name="Raha", age=30)

# Creating a teacher
sara = Teacher(name="Sara", age=25)

# Creating a worker
taha = Worker(name="Taha", age=22)

print(f"Total number of people: {len(Person.instances)}")
for p in Person.instances:
    print(f"- {p.name} ({p.get_job()}), Level: {p.level}")

# Creating a mine
kavir_mine = Mine(name="Kavir Mine")

# Creating a school
danesh_school = School(name="Danesh School")

# Creating a company
pishro_company = Company(name="Pishro Company")

print(f"\nTotal number of workplaces: {len(WorkPlace.instances)}")
for wp in WorkPlace.instances:
    print(f"- {wp.name} ({wp.get_expertise()}), Level: {wp.level}, Initial Capacity: {wp.capacity}")


try:
    kavir_mine.hire(taha)
    print(f"\n{taha.name} was hired at {taha.work_place.name}.")

    danesh_school.hire(sara)
    print(f"{sara.name} was hired at {sara.work_place.name}.")

    pishro_company.hire(raha)
    print(f"{raha.name} was hired at {raha.work_place.name}.")

    print(f"Employees of {pishro_company.name}: {[e.name for e in pishro_company.employees]}")

    # Attempting to hire beyond capacity
    kamran = Engineer(name="Kamran", age=35)
    pishro_company.hire(kamran) # This line would raise an error

except WorkPlaceIsFull as e:
    print(f"Hiring error: {e}")


print(f"\nInitial level of {raha.name}: {raha.level}")
raha.upgrade()
print(f"New level of {raha.name}: {raha.level}")

print(f"\nInitial level and capacity of {kavir_mine.name}: Level {kavir_mine.level}, Capacity {kavir_mine.capacity}")
kavir_mine.upgrade()
print(f"New level and capacity of {kavir_mine.name}: Level {kavir_mine.level}, Capacity {kavir_mine.capacity}")


taha_base_income = taha.calc_income()
print(f"\nBase daily income for {taha.name}: {taha_base_income}")

taha_life_cost = taha.calc_life_cost()
print(f"Daily living cost for {taha.name}: {taha_life_cost}")

taha_net_daily = taha.calc()
print(f"Net daily financial status for {taha.name}: {taha_net_daily}")


mine_maintenance_cost = kavir_mine.calc_costs()
print(f"\nDaily maintenance cost for {kavir_mine.name}: {mine_maintenance_cost}")

mine_net_daily = kavir_mine.calc()
print(f"Net daily financial status for {kavir_mine.name}: {mine_net_daily}")


