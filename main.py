import runpy
print("Do you want to run the data generation, training the model, or prediction file?")
choice = input("Enter '1' for Data Generation, '2' for Training the Model, or '3' for Prediction: ")
if choice == '1':
    print("Do you want to run two finger or three finger data generation?")
    finger_choice = input("Enter '2' for Two Finger or '3' for Three Finger: ")
    if finger_choice == '2':
        runpy.run_path("simulation_DataGeneration/2FingerGripper_Block.py")
        
    elif finger_choice == '3':
        print("Do you want to run three finger gripper with Block or Duck?")
        object_choice = input("Enter 'B' for Block or 'D' for Duck: ")
        if object_choice.upper() == 'B':
            runpy.run_path("simulation_DataGeneration/3FingerGripper_Block.py")
        elif object_choice.upper() == 'D':
            runpy.run_path("simulation_DataGeneration/3FingerGripper_Duck.py")
        else:
            print("Invalid choice. Please enter 'B' or 'D'.")
    else:
        print("Invalid choice. Please enter '2' or '3'.")
elif choice == '2':
    runpy.run_path("classifier/ClassifierModel.py")
elif choice == '3':
    print("Do you want to run two finger or three finger prediction?")
    finger_choice = input("Enter '2' for Two Finger or '3' for Three Finger: ")
    if finger_choice == '2':
        runpy.run_path("simulation_Prediction/Prediction_2FingerGripper_Block.py")
    elif finger_choice == '3':
        print("Do you want to run three finger gripper with Block or Duck?")
        object_choice = input("Enter 'B' for Block or 'D' for Duck: ")
        if object_choice.upper() == 'B':
            runpy.run_path("simulation_Prediction/Prediction_3FingerGripper_Block.py")
        elif object_choice.upper() == 'D':
            runpy.run_path("simulation_Prediction/Prediction_3FingerGripper_Duck.py")
        else:
            print("Invalid choice. Please enter 'B' or 'D'.")
    else:
        print("Invalid choice. Please enter '2' or '3'.")
else:
    print("Invalid choice. Please enter '1', '2', or '3'.")