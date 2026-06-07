
from flask import Flask, request, render_template_string

app = Flask(__name__)

# ============================================================
# MIGUEL YT - VERSÃO OFFLINE / TESTE
# ============================================================
# Esta versão NÃO depende de API externa.
# Ela serve para testar interface, fluxo, abas e lógica do site
# antes de conectar com a versão oficial.
# ============================================================


HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Miguel YT - Análise de Canais</title>

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: #080b12;
            color: #ffffff;
        }

        .page {
            min-height: 100vh;
            background:
                radial-gradient(circle at top left, rgba(255, 0, 90, 0.18), transparent 35%),
                radial-gradient(circle at top right, rgba(0, 200, 255, 0.15), transparent 35%),
                #080b12;
            padding: 24px 16px;
        }

        .container {
            width: 100%;
            max-width: 980px;
            margin: 0 auto;
        }

        .hero {
            text-align: center;
            padding: 30px 10px 25px;
        }

        .badge {
            display: inline-block;
            padding: 8px 14px;
            border-radius: 999px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.12);
            color: #d7e7ff;
            font-size: 14px;
            margin-bottom: 18px;
        }

        h1 {
            font-size: 42px;
            margin: 0;
            line-height: 1.1;
        }

        .gradient-text {
            background: linear-gradient(90deg, #ff2d75, #35d3ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            max-width: 760px;
            margin: 18px auto 0;
            color: #b7c0d1;
            font-size: 18px;
            line-height: 1.6;
        }

        .card {
            background: rgba(255,255,255,0.07);
            border: 1px solid rgba(255,255,255,0.12);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.35);
            backdrop-filter: blur(10px);
        }

        .form-area {
            margin-top: 20px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 10px;
            color: #ffffff;
        }

        input {
            width: 100%;
            padding: 16px;
            border-radius: 14px;
            border: 1px solid rgba(255,255,255,0.18);
            background: rgba(0,0,0,0.25);
            color: #ffffff;
            font-size: 16px;
            outline: none;
        }

        input:focus {
            border-color: #35d3ff;
            box-shadow: 0 0 0 3px rgba(53, 211, 255, 0.14);
        }

        button {
            width: 100%;
            margin-top: 16px;
            padding: 16px;
            border: none;
            border-radius: 14px;
            background: linear-gradient(90deg, #ff2d75, #35d3ff);
            color: #ffffff;
            font-size: 17px;
            font-weight: bold;
            cursor: pointer;
        }

        button:hover {
            opacity: 0.93;
        }

        .note {
            margin-top: 14px;
            color: #9ba8bd;
            font-size: 14px;
            line-height: 1.5;
        }

        .result {
            margin-top: 28px;
        }

        .tabs {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            margin-bottom: 18px;
        }

        .tab-button {
            padding: 13px 10px;
            border-radius: 12px;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.12);
            color: #dce7ff;
            font-weight: bold;
            cursor: pointer;
            text-align: center;
            font-size: 14px;
        }

        .tab-button.active {
            background: linear-gradient(90deg, rgba(255,45,117,0.9), rgba(53,211,255,0.9));
            color: #ffffff;
        }

        .tab-content {
            display: none;
            background: rgba(0,0,0,0.22);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 18px;
            padding: 22px;
        }

        .tab-content.active {
            display: block;
        }

        .tab-content h2 {
            margin-top: 0;
            font-size: 24px;
        }

        .tab-content h3 {
            color: #35d3ff;
            margin-top: 24px;
        }

        .tab-content p {
            color: #d1d8e6;
            line-height: 1.7;
        }

        .tab-content ul {
            padding-left: 20px;
        }

        .tab-content li {
            margin-bottom: 10px;
            color: #d1d8e6;
            line-height: 1.6;
        }

        .script-box {
            background: rgba(255,255,255,0.08);
            border-left: 4px solid #ff2d75;
            padding: 18px;
            border-radius: 12px;
            margin-top: 14px;
            color: #ffffff;
            line-height: 1.7;
        }

        .shorts-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 14px;
            margin-top: 15px;
        }

        .short-card {
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.10);
            border-radius: 16px;
            padding: 16px;
        }

        .short-card strong {
            color: #ffffff;
        }

        .footer {
            text-align: center;
            color: #7f8ca3;
            margin-top: 26px;
            font-size: 13px;
        }

        @media (max-width: 720px) {
            h1 {
                font-size: 34px;
            }

            .subtitle {
                font-size: 16px;
            }

            .tabs {
                grid-template-columns: 1fr 1fr;
            }

            .shorts-grid {
                grid-template-columns: 1fr;
            }

            .card {
                padding: 18px;
            }
        }
    </style>
</head>

<body>
    <div class="page">
        <div class="container">

            <section class="hero">
                <div class="badge">Versão Offline / Teste</div>

                <h1>
                    Miguel <span class="gradient-text">YT</span>
                </h1>

                <p class="subtitle">
                    Ferramenta inteligente para analisar canais do YouTube, encontrar pontos fortes,
                    corrigir erros e gerar ideias de conteúdo com foco em crescimento.
                </p>
            </section>

            <section class="card">
                <form method="POST" class="form-area">
                    <label for="canal">Digite o nome do canal:</label>

                    <input
                        type="text"
                        id="canal"
                        name="canal"
                        placeholder="Exemplo: Receita em 60s"
                        value="{{ canal }}"
                        required
                    >

                    <button type="submit">Analisar Canal</button>

                    <p class="note">
                        Esta versão é offline/teste. Ela ainda não consulta a API do YouTube.
                        O objetivo é validar a interface, as abas e o fluxo antes de conectar com a versão oficial.
                    </p>
                </form>

                {% if analisado %}
                <div class="result">

                    <div class="tabs">
                        <div class="tab-button active" onclick="openTab('abaA', this)">Aba A<br>Visão Geral</div>
                        <div class="tab-button" onclick="openTab('abaB', this)">Aba B<br>Melhorias</div>
                        <div class="tab-button" onclick="openTab('abaC', this)">Aba C<br>Script</div>
                        <div class="tab-button" onclick="openTab('abaD', this)">Aba D<br>Shorts</div>
                    </div>

                    <div id="abaA" class="tab-content active">
                        <h2>Aba A — Visão Geral do Canal</h2>

                        <p>
                            Canal analisado:
                            <strong>{{ canal }}</strong>
                        </p>

                        <p>
                            O canal possui potencial para crescer se trabalhar com clareza de nicho,
                            frequência de postagem, títulos fortes e conteúdos com promessa direta.
                        </p>

                        <h3>Diagnóstico inicial</h3>

                        <ul>
                            <li>O canal precisa deixar claro qual transformação entrega para o público.</li>
                            <li>Os conteúdos devem ter títulos mais específicos e fáceis de entender.</li>
                            <li>A estratégia precisa focar em vídeos curtos, diretos e com gancho forte nos primeiros segundos.</li>
                            <li>A identidade visual deve ser simples, reconhecível e repetível.</li>
                        </ul>
                    </div>

                    <div id="abaB" class="tab-content">
                        <h2>Aba B — Pontos Positivos e Pontos de Melhoria</h2>

                        <h3>Pontos positivos</h3>

                        <ul>
                            <li>Existe espaço para posicionamento forte dentro do nicho.</li>
                            <li>O formato pode funcionar bem em vídeos curtos.</li>
                            <li>O canal pode criar uma rotina de conteúdos fáceis de produzir.</li>
                            <li>Há potencial para transformar temas simples em conteúdos virais.</li>
                        </ul>

                        <h3>Pontos que precisam melhorar</h3>

                        <ul>
                            <li>Melhorar a promessa dos títulos.</li>
                            <li>Criar thumbnails mais claras e com menos informação.</li>
                            <li>Evitar introduções longas.</li>
                            <li>Usar chamadas mais fortes nos primeiros 3 segundos.</li>
                            <li>Finalizar os vídeos com convite direto para o próximo conteúdo.</li>
                        </ul>
                    </div>

                    <div id="abaC" class="tab-content">
                        <h2>Aba C — Roteiro Campeão</h2>

                        <p>
                            Abaixo está um modelo de roteiro curto que pode ser adaptado para o canal
                            <strong>{{ canal }}</strong>.
                        </p>

                        <div class="script-box">
                            <strong>Gancho inicial:</strong><br>
                            Você está cometendo esse erro sem perceber e isso pode estar travando o crescimento do seu canal.
                            <br><br>

                            <strong>Desenvolvimento:</strong><br>
                            Muitos criadores postam vídeos sem pensar na promessa principal.
                            Antes de gravar, responda: por que alguém deveria assistir esse conteúdo até o final?
                            Se a resposta não for clara, o vídeo perde força.
                            <br><br>

                            <strong>Virada estratégica:</strong><br>
                            O segredo é criar vídeos com uma promessa simples, rápida e direta.
                            Quanto mais fácil for entender o benefício, maior a chance da pessoa clicar e assistir.
                            <br><br>

                            <strong>Final:</strong><br>
                            Se você quer crescer no YouTube, comece ajustando seus títulos, seus primeiros segundos
                            e a clareza da sua mensagem.
                        </div>
                    </div>

                    <div id="abaD" class="tab-content">
                        <h2>Aba D — Ideias de Shorts</h2>

                        <p>
                            Esta aba será usada depois para transformar o roteiro campeão em ideias de Shorts.
                        </p>

                        <div class="shorts-grid">

                            <div class="short-card">
                                <strong>Short 1</strong>
                                <p>O erro que trava o crescimento de canais pequenos.</p>
                            </div>

                            <div class="short-card">
                                <strong>Short 2</strong>
                                <p>Como criar um título que faz a pessoa clicar.</p>
                            </div>

                            <div class="short-card">
                                <strong>Short 3</strong>
                                <p>Os primeiros 3 segundos decidem se seu vídeo vai performar.</p>
                            </div>

                            <div class="short-card">
                                <strong>Short 4</strong>
                                <p>Como transformar uma ideia simples em conteúdo viral.</p>
                            </div>

                        </div>

                        <h3>Próxima evolução desta aba</h3>

                        <ul>
                            <li>Gerar Shorts automaticamente a partir do roteiro.</li>
                            <li>Criar título, legenda e descrição para cada Short.</li>
                            <li>Separar cenas por fala.</li>
                            <li>Preparar estrutura para voz, imagem e vídeo.</li>
                        </ul>
                    </div>

                </div>
                {% endif %}
            </section>

            <div class="footer">
                Miguel YT — Ambiente offline de teste antes da versão oficial
            </div>

        </div>
    </div>

    <script>
        function openTab(tabId, element) {
            var contents = document.querySelectorAll('.tab-content');
            var buttons = document.querySelectorAll('.tab-button');

            contents.forEach(function(content) {
                content.classList.remove('active');
            });

            buttons.forEach(function(button) {
                button.classList.remove('active');
            });

            document.getElementById(tabId).classList.add('active');
            element.classList.add('active');
        }
    </script>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def index():
    canal = ""
    analisado = False

    if request.method == "POST":
        canal = request.form.get("canal", "").strip()

        if canal:
            analisado = True

    return render_template_string(
        HTML,
        canal=canal,
        analisado=analisado
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
