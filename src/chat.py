from search import search_prompt

def main():
    print("#" * 73)
    print("# Desafio de Ingestão e Busca Semântica com LangChain e Postgres - Chat #")
    print("# Digite sua pergunta ou digite 'sair' para encerrar o chat.            #")
    print("#" * 73 + "\n")
    while True:
        pergunta = input("Pergunta: ")
        if pergunta.lower() == "sair":
            print("Chat encerrado.")
            break
        response = search_prompt(pergunta)
        print(f"Resposta: {response} \n")
        print("-" * 73 + "\n")

if __name__ == "__main__":
    main()