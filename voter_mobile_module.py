import list_of_name_age_id_mobile
def print_voter_mobile():
    for i in range(3):
        mobile=int(input("Enter the voters mobile:-"))
        mobile_list=list_of_name_age_id_mobile.mobile_list.append(mobile)

#for i in range(3):
print(list_of_name_age_id_mobile.mobile_list)
