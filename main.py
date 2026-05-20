print("=================================")
print("   MOVIE RECOMMENDATION SYSTEM   ")
print("=================================")

print("\n1. Load Data")
print("2. Clean Data")
print("3. EDA Analysis")
print("4. Visualization")
print("5. Recommendation System")
print("6. Exit")

while True:

    choice = input("\nEnter your choice: ")

    if choice == '1':
        import load_data

    elif choice == '2':
        import clean_data

    elif choice == '3':
        import eda_analysis

    elif choice == '4':
        import visualization

    elif choice == '5':
        import recommendation_system

    elif choice == '6':
        print("Exiting Project... Bye 👋")
        break

    else:
        print("Invalid Choice ❌ Please try again")