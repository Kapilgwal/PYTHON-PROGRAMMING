def replaceElement(input_list: list[int], temp: list[int]) -> list[int]:
    temp.sort()
    ans = []
    value_to_index = {value: i for i, value in enumerate(temp)}

    for value in input_list:
        ans.append(value_to_index[value])
    
    return ans

def main():
    input_list = [20, 15, 26, 2, 98, 6]
    temp = input_list.copy()
    ans = replaceElement(input_list, temp)
    print(ans)

if __name__ == "__main__":
    main()
