import voter_name_module
import voter_age_module
import voter_id_module
import voter_mobile_module


def print_voter_details():
    print("calling all modulues ")
    print('---------------------')
    voter_name_module.print_voter_name()
    voter_age_module.print_voter_age()
    voter_id_module.print_voter_id()
    voter_mobile_module.print_voter_mobile()
    
if __name__=="__main__":
    print_voter_details()
