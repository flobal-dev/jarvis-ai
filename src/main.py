from rag import build_index, query

def main():
    print("Baue Index...")
    index = build_index()

    print("Jarvis bereit (exit zum Beenden)")

    while True:
        q = input("Du: ")
        if q.lower() == "exit":
            break

        response = query(index, q)
        print("Jarvis:", response)

if __name__ == "__main__":
    main()