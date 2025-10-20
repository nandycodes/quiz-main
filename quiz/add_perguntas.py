import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from quizapi.models import Pergunta

dados = [
   
    # FÁCEIS
   
    {"texto": "O que significa a sigla TI?", "nivel": "facil", "opcoes": ["Tecnologia da Informação", "Técnica Industrial", "Telecomunicação Integrada", "Teoria da Internet"], "resposta_correta": "Tecnologia da Informação"},
    {"texto": "Qual linguagem é usada para estruturar páginas web?", "nivel": "facil", "opcoes": ["HTML", "Python", "CSS", "SQL"], "resposta_correta": "HTML"},
    {"texto": "Qual é o sistema operacional mais usado em servidores?", "nivel": "facil", "opcoes": ["Linux", "Windows", "macOS", "Android"], "resposta_correta": "Linux"},
    {"texto": "Em Banco de Dados, o SQL é usado para?", "nivel": "facil", "opcoes": ["Manipular dados", "Criar imagens", "Editar vídeos", "Fazer login em redes"], "resposta_correta": "Manipular dados"},
    {"texto": "Qual é a função do CSS?", "nivel": "facil", "opcoes": ["Estilizar páginas web", "Fazer consultas em bancos de dados", "Criar servidores", "Executar códigos Python"], "resposta_correta": "Estilizar páginas web"},
    {"texto": "O que é um byte?", "nivel": "facil", "opcoes": ["Unidade de armazenamento de dados", "Linguagem de programação", "Erro de rede", "Tipo de vírus"], "resposta_correta": "Unidade de armazenamento de dados"},
    {"texto": "Qual comando do Git é usado para clonar um repositório?", "nivel": "facil", "opcoes": ["git clone", "git push", "git add", "git pull"], "resposta_correta": "git clone"},
    {"texto": "Qual dispositivo é usado para conectar redes diferentes?", "nivel": "facil", "opcoes": ["Roteador", "Monitor", "Teclado", "Placa de vídeo"], "resposta_correta": "Roteador"},
    {"texto": "Qual extensão pertence a arquivos Python?", "nivel": "facil", "opcoes": [".py", ".html", ".js", ".css"], "resposta_correta": ".py"},
    {"texto": "O que é um algoritmo?", "nivel": "facil", "opcoes": ["Sequência de instruções para resolver um problema", "Um tipo de vírus", "Um erro de software", "Um hardware de rede"], "resposta_correta": "Sequência de instruções para resolver um problema"},

    
    # MÉDIAS
    {"texto": "Qual sistema operacional popular é baseado no kernel Linux?", "nivel": "medio", "opcoes": ["Ubuntu", "Windows 11", "macOS", "FreeBSD"], "resposta_correta": "Ubuntu"},
    {"texto": "Em redes, o que significa IP?", "nivel": "medio", "opcoes": ["Internet Protocol", "Internal Program", "Integrated Platform", "Information Path"], "resposta_correta": "Internet Protocol"},
    {"texto": "Qual comando SQL é usado para atualizar registros?", "nivel": "medio", "opcoes": ["UPDATE", "SELECT", "INSERT", "DELETE"], "resposta_correta": "UPDATE"},
    {"texto": "O que é o front-end no desenvolvimento web?", "nivel": "medio", "opcoes": ["Parte visual da aplicação", "Servidor de banco de dados", "Gerenciador de usuários", "Camada de segurança"], "resposta_correta": "Parte visual da aplicação"},
    {"texto": "Qual protocolo é usado para envio de e-mails?", "nivel": "medio", "opcoes": ["SMTP", "HTTP", "FTP", "SNMP"], "resposta_correta": "SMTP"},
    {"texto": "Em programação, o que é um loop?", "nivel": "medio", "opcoes": ["Estrutura que repete instruções", "Um erro de compilação", "Um tipo de variável", "Um banco de dados"], "resposta_correta": "Estrutura que repete instruções"},
    {"texto": "Qual é o papel de um firewall?", "nivel": "medio", "opcoes": ["Proteger a rede contra acessos não autorizados", "Melhorar a velocidade da internet", "Armazenar senhas", "Gerar relatórios de rede"], "resposta_correta": "Proteger a rede contra acessos não autorizados"},
    {"texto": "Em banco de dados, o que é uma chave primária?", "nivel": "medio", "opcoes": ["Campo que identifica unicamente um registro", "Campo de texto livre", "Campo duplicado", "Campo de senha"], "resposta_correta": "Campo que identifica unicamente um registro"},
    {"texto": "O que significa IDE em programação?", "nivel": "medio", "opcoes": ["Integrated Development Environment", "Internet Data Exchange", "Interactive Design Editor", "Internal Database Engine"], "resposta_correta": "Integrated Development Environment"},
    {"texto": "O que é HTML5?", "nivel": "medio", "opcoes": ["Versão mais recente da linguagem de marcação web", "Uma linguagem de servidor", "Um sistema operacional", "Um banco de dados"], "resposta_correta": "Versão mais recente da linguagem de marcação web"},

    
    # DIFÍCEIS
    
    {"texto": "Qual das opções representa um modelo de rede em camadas?", "nivel": "dificil", "opcoes": ["Modelo OSI", "Modelo Binário", "Modelo Harvard", "Modelo RISC"], "resposta_correta": "Modelo OSI"},
    {"texto": "Em sistemas operacionais, o que é escalonamento de processos?", "nivel": "dificil", "opcoes": ["Técnica para gerenciar execução de processos", "Método de armazenamento de dados", "Processo de compressão de arquivos", "Protocolo de rede"], "resposta_correta": "Técnica para gerenciar execução de processos"},
    {"texto": "Qual normalização elimina dependências transitivas em banco de dados?", "nivel": "dificil", "opcoes": ["3ª Forma Normal", "1ª Forma Normal", "2ª Forma Normal", "Forma de Boyce-Codd"], "resposta_correta": "3ª Forma Normal"},
    {"texto": "Em redes, o protocolo HTTPS utiliza qual camada adicional em relação ao HTTP?", "nivel": "dificil", "opcoes": ["Camada de segurança (SSL/TLS)", "Camada de transporte", "Camada de aplicação", "Camada de enlace"], "resposta_correta": "Camada de segurança (SSL/TLS)"},
    {"texto": "Qual é o principal objetivo de uma transação ACID em banco de dados?", "nivel": "dificil", "opcoes": ["Garantir consistência e integridade dos dados", "Aumentar velocidade de leitura", "Reduzir redundância de tabelas", "Melhorar interface do usuário"], "resposta_correta": "Garantir consistência e integridade dos dados"},
    {"texto": "Em lógica de programação, o que caracteriza a recursão?", "nivel": "dificil", "opcoes": ["Função que chama a si mesma", "Função que nunca retorna valor", "Loop infinito", "Estrutura condicional"], "resposta_correta": "Função que chama a si mesma"},
    {"texto": "Em segurança da informação, o que é phishing?", "nivel": "dificil", "opcoes": ["Técnica de fraude para roubo de dados", "Tipo de firewall", "Protocolo de segurança", "Ataque físico ao servidor"], "resposta_correta": "Técnica de fraude para roubo de dados"},
    {"texto": "Qual é o papel do DNS na internet?", "nivel": "dificil", "opcoes": ["Traduzir nomes de domínio em endereços IP", "Armazenar arquivos de rede", "Bloquear pacotes", "Gerar senhas"], "resposta_correta": "Traduzir nomes de domínio em endereços IP"},
    {"texto": "Em sistemas operacionais, o que é um deadlock?", "nivel": "dificil", "opcoes": ["Situação em que processos ficam bloqueados aguardando recursos", "Erro de compilação", "Falha de hardware", "Perda de pacote na rede"], "resposta_correta": "Situação em que processos ficam bloqueados aguardando recursos"},
    {"texto": "Qual conceito define a capacidade de um sistema continuar funcionando mesmo com falhas?", "nivel": "dificil", "opcoes": ["Tolerância a falhas", "Multiprocessamento", "Virtualização", "Concorrência"], "resposta_correta": "Tolerância a falhas"},
]

for item in dados:
    Pergunta.objects.create(**item)

print("30 perguntas adicionadas com sucesso!") #teste
