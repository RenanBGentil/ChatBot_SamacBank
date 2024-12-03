from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


# Função que simula o chatbot (resposta simples)
def obter_resposta(mensagem):
    respostas = {
"Como faço para encerrar minha conta?":
        "Para encerrar sua conta, basta clicar no botão 'Encerrar Conta' na página de login, espero que volte e desculpe qualquer incôveniente.",
        "meu celular foi roubado, como desativo o app do banco?":
        "Ligue para nos ou vai para nossas agências",
        "posso resgatar meus investimentos a qualquer momento?":
        "Sim, você pode resgatar seus investimentos a qualquer momento. Para resgatar seus investimentos, basta seguir as instruções fornecidas no nosso site.",
        "posso renegociar minha dívida?":
        "Sim, você pode renegociar sua dívida com nosso banco. Por favor, entre em contato conosco para mais informações.",
        "como vejo o rendimento dos meus investimentos?":
        "Para obter o rendimento dos seus investimentos, você pode utilizar ferramentas de análise de dados, como o Yahoo Finance ou o B3.com.",
        "recebi um e-mail suspeito, como saber se é do banco?":
        "Para saber se é do banco, você precisa verificar se o e-mail é de um banco conhecido. Você pode fazer isso verificando se o e-mail tem um endereço de e-mail relacionado a um banco conhecido",
        "como garantir que minha conta ta segura?":
        "Para garantir que sua conta esteja segura, siga os seguintes passos: 1. Crie uma senha forte e única para sua conta. 2. Não compartilhe sua senha com ninguém. 3. Use sites confiaveis para entrar na sua conta. 4. Ative a autenticação de dois fatores",
        "o que você gosta de fazer":
        "Eu gosto de ajudar pessoas e encontrar respostas para sua perguntas.",
        "oi tudo bem?":
        "Olá! Estou muito bem. Como posso ajudar você hoje?",
        "quais são as taxas de juros para empréstimos?":
        "A taxa de juros do nosso banco é 5,99% ao mês.",
        "qual é o prazo de pagamento?":
        "O prazo de pagamento é de até 3 meses.",
        "recebi um e-mail suspeito como saber se é do banco?":
        "Você pode ligar para seu gerente ou para o atendimento ao cliente.",
        "qual o limite do me cartão?":
        "O limite do seu cartão é de R$ 3.500,00.",
        "meu cartão foi roubado/perdido, como bloquear?":
        "Basta ir no nosso aplicativo na aba meu cartão -> Bloquear cartão -> Meu cartão -> Pedir um novo cartão.",
        "como fazer um empréstimo?":
        "Para fazer um empréstimo, você precisa seguir algumas etapas. Primeiro clique em um botão de empréstimo e escolha a opção que melhor se encaixa com você. Depois, preencha o formulário de empréstimo e envie-o para nossa equipe de atendimento. Aguarde a resposta do nosso atendimento.",
        "como faço um pix?":
        "Para fazer um pix, você precisa seguir os seguintes passos: Abrir o aplicativo da sua conta bancária, clicar em 'Pix' -> Transferência -> Insira a chave Pix -> Enviar",
        "como fazer um pix?":
        "Para fazer um pix, você precisa seguir os seguintes passos: Abrir o aplicativo da sua conta bancária, clicar em 'Pix' -> Transferência -> Insira a chave Pix -> Enviar",
        "como recuperar minha senha?":
        "Basta você acessar nosso aplicativo ou site e clicar em recuperar senha",
        "como posso alterar meus dados cadastrais?":
        "Para alterar seus dados cadastrais, basta acessar o site e alterar suas informações.",
        "qual o numero da minha agência?":
        "O número da sua agência é: 0000-1.",
        "qual é meu saldo do banco?":
        "Seu saldo é de R$ 5.489,00. Obrigado por utilizar nossos serviço.",
        "qual é a taxa de anuidade?":
        "A taxa de anuidade é de R$ 10,00. Obrigado por utilizar nosso serviços",
        "voces disponibilizam serviços de qualidade?":
        "Sim! Eu disponibilizo serviços de qualidade, garantindo que os clientes tenham o melhor atendimento comigo, seu assistente virtual Sam.",
        "conta corrente":
        "Sua conta corrente está com R$10.000,00 de saldo.",
        "oi":
        "Olá! Como posso te ajudar hoje?",
        "olá":
        "Oi! Em que posso ajudar você no SAMAC Bank?",
        "tchau":
        "Tchau! Até logo e tenha um ótimo dia.",
        "como você está?":
        "Estou ótimo, obrigado por perguntar! Como posso ajudar você?",
        "qual o saldo da minha conta?":
        "Para verificar seu saldo, por favor, faça login em sua conta.",
        "quais são os tipos de conta que o banco oferece?":
        "O SAMAC Bank oferece contas correntes e contas poupança, além de diversas opções de investimentos.",
        "qual o limite do meu cartão de crédito?":
        "Para verificar o limite do seu cartão de crédito, entre em contato com nosso atendimento ou acesse o app do SAMAC Bank.",
        "como posso abrir uma conta?":
        "Você pode abrir uma conta no SAMAC Bank diretamente no nosso site ou em uma de nossas agências.",
        "vocês têm serviços de câmbio?":
        "Sim, oferecemos serviços de câmbio para diversos tipos de moeda. Consulte nossa página de câmbio para mais informações.",
        "quais são os tipos de investimentos disponíveis?":
        "O SAMAC Bank oferece opções de investimentos como CDB, LCI, LCA, fundos de investimento e previdência privada.",
        "como faço para transferir dinheiro?":
        "Você pode realizar transferências através do nosso site ou aplicativo, usando TED ou PIX.",
        "qual a taxa de juros do empréstimo pessoal?":
        "As taxas de juros variam de acordo com o perfil do cliente. Entre em contato com nosso setor de crédito para mais detalhes.",
        "vocês oferecem cartão de crédito sem anuidade?":
        "Sim, temos opções de cartão de crédito sem anuidade. Consulte as condições no nosso site.",
        "qual o horário de funcionamento das agências?":
        "Nossas agências funcionam de segunda a sexta-feira, das 9h às 16h.",
        "como posso bloquear meu cartão?":
        "Se precisar bloquear seu cartão, entre em contato imediatamente com nossa central de atendimento ou pelo aplicativo.",
        "quais documentos são necessários para abrir uma conta?":
        "Para abrir uma conta no SAMAC Bank, você precisará de um documento de identidade, CPF e comprovante de residência.",
        "qual é o saldo da minha conta?":
        "Infelizmente, não podemos fornecer informações sobre saldo através do chatbot. Por favor, consulte seu extrato bancário ou use nosso app.",
        "como faço para bloquear meu cartão?":
        "Para bloquear seu cartão, por favor, entre em contato com nosso suporte pelo número 0800-123-4567 ou acesse sua conta online.",
        "vocês oferecem empréstimos pessoais?":
        "Sim, oferecemos empréstimos pessoais com taxas de juros acessíveis. Por favor, acesse nossa página de empréstimos para mais informações.",
        "qual é o prazo para aprovação de crédito?":
        "O prazo para aprovação de crédito é de 2 a 5 dias úteis, dependendo da análise de crédito e documentação.",
    }
    return respostas.get(
        mensagem.lower(),
        "Desculpe, não entendi sua pergunta. Posso ajudar com mais alguma coisa?"
    )


# Rota para renderizar o HTML
@app.route('/')
def index():
    return render_template('index.html')


# Rota para receber a mensagem do usuário e enviar a resposta do chatbot
@app.route('/resposta', methods=['POST'])
def resposta():
    usuario_msg = request.json.get('mensagem')
    resposta_chatbot = obter_resposta(usuario_msg)
    return jsonify({'resposta': resposta_chatbot})


# O Replit utiliza a variável de ambiente `PORT`, então usaremos ela para rodar o Flask
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
