# main
def main():


    # Create Instructors Dictionary 
    instructor = {'CS101': 'Haynes', 'CS102': 'Alvarado', 'CS103': 'Rich', 'NT110': 'Burke', 'CM241': 'Lee'}

    # Create Room Number Dictionary
    room_num = {'CS101': '3004', 'CS102': '4501', 'CS103': '6755', 'NT110': '1244', 'CM241': '1411'}

    # Create Meeting Time Dictionary
    meeting_time = {'CS101': '8:00 a.m.', 'CS102': '9:00 a.m.', 'CS103': '10:00 a.m.', 'NT110': '11:00 a.m.', 'CM241': '1:00 p.m.'}




    # Input the Course that user wants Information about
    id_input = input('Please enter course ID: ')

    # Call information in dictionary through "get" which is linked to the input

    xyz = instructor.get(id_input), room_num.get(id_input), meeting_time.get(id_input)

    #Print 
    print(xyz)
# Call the Main
main()

