from smart_fridge import recipes , pantry

# desplay recipes 1 way
# d_play_recipes = {}
# for index , key in enumerate(recipes):
#     d_play_recipes[str(index+1)] = key

# for key , value in d_play_recipes.items():
#     print(key,value)

# desplay recipes 2 way
d_play_recipes = {str(index + 1) : value for index , value in enumerate(recipes)}
need_to_buy = {}

print(pantry)
while True:

    print("please choose your recipes")
    print("-"*80)

    for key , value in d_play_recipes.items():
        print(key,":",value)

    choice = input(">>> ")

    if choice == '0':
        break
    elif choice in d_play_recipes:
        selected_item = d_play_recipes[choice]
        print(f"You have selected {selected_item}")
        print(f"Let's check ingredients...")
        ingredients = recipes[selected_item]
        for items , need_quntity in ingredients.items(): 
            # print(items,chr(9),":",quntity)
            total_quntity = pantry[items]
            if need_quntity < total_quntity:
                print("{} OK".format(items))
            else:
                need = need_quntity-total_quntity
                print("we have only {} {}, we need to buy {} more.".format(total_quntity,items,need))
                need_to_buy[items] = need

        print("you need to buy...")
        for item,quntity in need_to_buy.items():
            print("{:<15} \t{:^}".format(item,quntity))