def num_boats(people, limit):
    people.sort()
    i, j = 0, len(people) - 1
    boats = 0
    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
            j -= 1
            boats += 1
        else:
            j -= 1
            boats += 1
    return boats

if __name__ == "__main__":
    print(num_boats([2,2,1,3], 4))
    print(num_boats([2,2,1,3,1], 3))