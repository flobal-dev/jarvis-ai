from rag import build_index, query

def main():
    print("Baue Index (LOCAL)...")
    index, llm = build_index()

    print("Jarvis LOCAL bereit 😎")

    while True:
        q = input("Du: ")
        if q.lower() == "exit":
            break

        response = query(index, llm, q)
        print("Jarvis:", response)


if __name__ == "__main__":
    main()