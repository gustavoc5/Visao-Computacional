import kagglehub

# Baixar a versão mais recente do FER-2013+
path = kagglehub.dataset_download("subhaditya/fer2013plus")

print("FER2013+ salvo em:", path)
# Verificar se o download foi bem-sucedido
if path:
    print("Download concluído com sucesso!")