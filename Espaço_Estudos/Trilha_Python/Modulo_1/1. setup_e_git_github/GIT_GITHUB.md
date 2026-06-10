# Comandos Git e Git Hub


# **GIT**

### 🏁 Comando de Inicialização do GIT:

    git init

Após inicializar o GIT na máquina, podemos inserir nossos arquivos ao **git staging area** utilizando o comando abaixo:

    git add <arquivo>   ou   git add . (para adicionar todos os arquivos do diretório)

<span style="color:red">
<b>Atenção:</b> 
</span>
Os arquivos irão para um processo de **stage área** (área de preparação), conforme mostrado na imagem abaixo:

![alt text](<Imagens/git_github/Estudo Git.jpg>)


O comando principal para entender o que está acontecendo no seu repositório local é o **git status**. Ele funciona como um "raio-X", mostrando o estado atual dos seus arquivos em relação às três principais áreas do Git: o diretório de trabalho, a Stage Area (área de preparação) e o Repositório (Branch atual).

    git status

Ao executar este comando, o Git pode retornar diferentes estados para os seus arquivos. Veja os principais:

**1 - On branch [nome_da_branch]**

* Indica em qual **branch** (ramificação de desenvolvimento) você está trabalhando no momento (por exemplo, **main** ou **master**). Todas as informações exibidas abaixo dessa linha serão referentes a essa branch específica.

**2 - Untracked files (Arquivos Não Monitorados)**

* O que significa: São arquivos novos que foram criados na sua pasta, mas que o Git ainda não começou a rastrear. Eles existem localmente, mas não fazem parte do histórico do projeto e não estão na Stage Area.

* Identificação visual: Por padrão, o Git Bash exibe esses arquivos na cor vermelha.

* Como avançar: Para que o Git comece a monitorá-los, você precisa utilizá-lo junto com o comando git add [nome_do_arquivo].

**3 - Changes not staged for commit (Modificações não preparadas)**

* O que significa: Arquivos que o Git já monitorava anteriormente, mas que sofreram alterações recentes que ainda não foram enviadas para a Stage Area.

* Identificação visual: Também ficam em <span style="color:red">**vermelho**</span> no Git Bash.

* Como avançar: Para que o Git comece a monitorá-los, você precisa utilizá-lo junto com o comando git add [nome_do_arquivo].

**4 - Changes to be committed (Alterações prontas para o Commit)**

* O que significa: Arquivos (novos ou modificados) que já foram adicionados à Stage Area (usando git add). Eles estão "na sala de espera", prontos para serem salvos permanentemente no próximo commit.

* Identificação visual: Ficam na cor <span style="color:green">**verde**</span> no Git Bash.

#### 💡 **Dica de Ouro:**

Se o terminal exibir a mensagem "nothing to commit, working tree clean", significa que todos os seus arquivos estão salvos e sincronizados com o repositório local na branch atual. Nenhum arquivo foi modificado ou criado desde o último commit.

### 💾 **Salvando as Alterações: O Commit e a Configuração Inicial**

Depois que os arquivos foram enviados para a **Stage Area** (ou seja, estão sinalizados em <span style="color:green">**verde**</span> no **_git status_**), eles estão prontos para serem salvos permanentemente no histórico do projeto. 

**Essa ação de salvar é chamada de Commit.**

No entanto, antes de fazer o seu primeiro commit, o Git exige que você se identifique. Isso acontece porque cada commit no Git fica registrado com o nome e o e-mail de quem fez a alteração, o que é fundamental para o trabalho em equipe.

### ⚙️ **Configuração Inicial**

Se você tentar fazer um commit sem essa configuração, o Git apresentará um erro. Para cadastrar sua identidade globalmente no sistema (você só precisa fazer isso uma vez no seu computador), utilize os seguintes comandos no Git Bash:

**1 - Configurar o Nome de Usuário:**

    git config --global user.name "Seu Nome Completo"

**2 - Configurar o E-mail:**

    git config --global user.email "seu.email@exemplo.com"


**⚠️ Importante:**

 Substitua "Seu Nome Completo" e "seu.email@exemplo.com" pelos seus dados reais (mantendo as aspas). Se você utiliza o GitHub, é altamente recomendável usar o mesmo e-mail cadastrado na sua conta de lá para que os commits fiquem vinculados corretamente ao seu perfil.

### 🔍 **Como verificar se a configuração deu certo?**

Se quiser conferir se o Git salvou os dados corretamente, você pode rodar os comandos sem passar nenhum valor ao final:

    git config user.name
    git config user.email


### 🔄 **Antes de Commitar**

#### **Removendo Arquivos da Stage Area (Desfazendo o git add)**

Imagine que você executou o comando **git add .**, mas enviou por engano um arquivo que não deveria ser salvo neste **commit**. Se você rodar o **git status**, verá esse arquivo listado em verde.

Para tirar esse arquivo da **"sala de espera" (Stage Area)** e devolvê-lo para o estado vermelho, sem apagar ou estragar o código dele, você tem duas opções dependendo da situação do arquivo:

**📥 Caso 1: O arquivo é NOVO (Untracked)**
<br>
Se o arquivo acabou de ser criado e nunca passou por um commit antes, o comando ideal é exatamente o que você sugeriu:

    git rm --cached nome_do_arquivo.txt

**O que ele faz:** O parâmetro --cached avisa ao Git para remover o arquivo apenas do índice de preparação (Stage). O arquivo físico continua intacto na sua pasta, mas volta a ficar vermelho (Untracked).

🔄 **Caso 2: O arquivo já existia e foi apenas MODIFICADO**
<br>
Se o arquivo já fazia parte do projeto e você apenas alterou algumas linhas dele e deu git add por engano, o Git moderno recomenda o comando restore:

    git restore --staged nome_do_arquivo.txt

**O que ele faz**: A flag --staged diz ao Git para "restaurar o estado do arquivo na Stage Area", tirando ele de lá. Suas modificações no código continuam salvas no seu computador, mas o arquivo volta a ficar vermelho (Changes not staged for commit).

**💡 Dica de Ouro do Terminal**

Você não precisa decorar esses comandos! Se você estiver na dúvida de como tirar um arquivo da Stage Area, basta rodar um simples git status. O próprio Git Bash exibe uma mensagem de ajuda em cima dos arquivos verdes dizendo exatamente qual comando usar:

    (use "git rm --cached <file>..." to unstage) ou (use "git restore --staged <file>..." to unstage)


### **🚀 Realizando o Commit**

Com a identidade configurada e os arquivos na **Stage Area** (sinalizados em <span style="color:green">**verde**</span> no **_git status_**), você finalmente pode criar o seu ponto de restauração no histórico do projeto.

Para salvar essas alterações permanentemente, utilize o comando:

    git commit -m "Mensagem descritiva do que foi feito"

#### 🔍 Entendendo o comando:

<span style="color:purple">**git commit:**</span> Informa ao Git que você quer salvar o estado atual dos arquivos que estavam na Stage Area.

<span style="color:purple">**-m**:</span></span> É a flag de "mensagem". Ela avisa ao Git que você vai passar a descrição do commit logo em seguida, entre aspas.

<span style="color:purple">**"Mensagem descritiva"**:</span></span> O texto descritivo do que foi alterado ou criado.

#### 💡**Boas Práticas para Mensagens de Commit**

A mensagem de commit é o "diário de bordo" do seu projeto. Evite mensagens genéricas como "ajustes" ou "código novo". Prefira mensagens que expliquem brevemente o que foi feito:

- 🟢 <span style="color:green">**Bom exemplo:**</span> *git commit -m "Cria estrutura inicial do script de automação"*
- 🟢 <span style="color:green">**Bom exemplo:**</span> *git commit -m "Corrige bug na leitura do arquivo de configuração"*
- 🔴 <span style="color:red">**Mau exemplo:**</span> *git commit -m "mudanças" ou git commit -m "teste123"

### 🔄 **O que acontece depois?**

Após rodar o comando com sucesso, se você executar o **_git status_** novamente, o terminal informará que não há nada pendente ("nothing to commit, working tree clean"). Isso significa que seu trabalho local foi salvo com sucesso!

### 📜 **Consultando o Histórico: _O git log_**

Depois de realizar um ou mais commits, você pode consultar o histórico de tudo o que foi salvo no seu repositório. O comando para navegar por essa **"linha do tempo"** do projeto é o **_git log_**.

    git log

Ao executar esse comando, o Git exibirá uma lista com todos os commits realizados, do mais recente para o mais antigo.

#### 🔍 **Entendendo a saída do comando**

Para cada commit cadastrado, o Git exibe quatro informações fundamentais:

- **ID do Commit (Hash):** Uma sequência longa de letras e números (ex: commit a1b2c3d4...). Esse código é a identidade única daquela alteração.
- **Autor:** O nome e o e-mail de quem realizou o commit (aqueles dados que você configurou no início!).
- **Data:** O dia, horário e fuso horário exatos em que o commit foi feito.
- **Mensagem:** O texto descritivo que você inseriu usando a flag -m.

💡 **Dicas Importantes de Navegação**

**🚪 Como sair da tela do log?**

Se o seu histórico de commits for muito longo, o Git Bash abrirá uma tela de leitura e exibirá a palavra (END) ou um sinal de : no final. Para sair dessa tela e voltar a digitar comandos, basta apertar a **tecla Q** no teclado.

**🗺️ Visualização Compacta (Uma Linha):**

Para projetos maiores, o git log padrão pode ocupar muito espaço na tela. Você pode usar uma variação que mostra apenas o ID resumido e a mensagem de cada commit:

    git log --oneline


### 📍 **Entendendo o ponteiro HEAD -> master (ou HEAD -> main)**

Quando você executa o comando **_git log_**, logo na primeira linha do commit mais recente, você verá uma indicação parecida com esta:

<span style="color:purple">**commit a1b2c3d4... (HEAD -> master)** </span>

Esses dois termos funcionam como placas de sinalização para o Git saber exatamente onde você está no histórico. 

**Veja o que cada um significa:**

- **master (ou main):** É o nome da branch (ramificação) atual onde você está trabalhando.

- **HEAD:** É o "ponteiro" ou o indicador de posição atual do Git. Pense na HEAD como a cabeça de leitura de um antigo toca-discos ou o cursor de texto de um documento. Ela aponta exatamente para o commit em que você se encontra neste exato momento.

<br>

🧭 **O que a seta (->) está nos dizendo?**

A seta indica que a sua HEAD está apontando para a branch master.

**Em termos práticos, a expressão HEAD -> master significa:**

"Você está atualmente na branch master, e o seu próximo commit será colado logo após este commit onde a HEAD está apontando."


#### 💡 **Por que isso é importante?**

Se no futuro você precisar **_"viajar no tempo"_** para examinar um commit antigo do seu projeto, a palavra **HEAD** vai se mover para esse commit antigo, enquanto a palavra master continuará lá na frente, no último commit feito. É assim que você descobre visualmente se está olhando para o presente ou para o passado do seu código.


### ⏳ **Viajando no Tempo: O git checkout**

Uma das maiores vantagens do Git é a possibilidade de **"voltar no tempo"* para ver como seu projeto estava em um momento específico do passado, sem o risco de apagar ou estragar o código atual. Para fazer essa viagem, utilizamos o comando abaixo:

    git checkout

#### Segue passo a passo da viajem no tempo:


🧭 **Passo 1: Descubra para onde você quer ir**

Antes de voltar no tempo, você precisa do ID (Hash) do commit para onde deseja viajar. Use o comando que aprendemos na seção anterior para listar o histórico de forma compacta:

    git log --oneline

O terminal vai listar seus commits assim:

<span style="color:purple">**e4f5g6h Corrigido bug na automação**</span><br>
<span style="color:purple">**c3d4e5f Adicionado novo layout do painel**</span><br>
<span style="color:purple">**a1b2c3d Commit inicial do projeto**</span>

🚀 **Passo 2: Executando o comando**

Imagine que você quer voltar para o momento do Commit inicial **(a1b2c3)** para checar como o código era naquela época. Basta digitar **git checkout** seguido pelos **6 primeiros caracteres** do ID daquele commit:

    git checkout a1b2c3

Ao fazer isso, os arquivos na sua pasta física (no seu computador) vão mudar instantaneamente, voltando exatamente ao estado em que estavam no dia daquele commit!

⚠️ **O Estado "Detached HEAD" (HEAD Desconectada)**

Se você rodar o **git log --oneline** após viajar para o passado, notará que a sinalização mudou:

<span style="color:purple">**commit a1b2c3d... (HEAD)**</span> (repare que o -> master sumiu!)

Isso significa que você está no modo de <span style="color:purple">**apenas leitura**</span> do passado. O Git avisa que você está com a <span style="color:purple">**"HEAD desconectada"</span>**. Você pode olhar o código e fazer testes, mas não deve fazer novos commits aqui, pois eles ficariam <span style="color:red">**perdidos no tempo**</span>.


🏠 **Como voltar para o Presente?**

Depois de "passear" pelo passado, você vai querer voltar para a versão mais recente do código. Como o seu histórico continua avançando (o passado não apaga o futuro), você precisa dizer ao Git: **"Me leve de volta para o último commit da branch master"**.

Para isso, usamos o comando **_git switch_**, que é uma forma mais moderna e segura de fazer isso (embora **_git checkout master_** também funcione):

    git switch master

Ou a forma antiga:

    git checkout master

Isso fará com que os arquivos voltem ao estado atual e a sua HEAD volte a apontar para a ponta da linha do tempo.


## 🌀 **Branch e Merge**

![alt text](<Imagens/git_github/Branch_Merge.png>)

### **Branches**

As branches (ou ramificações) são linhas de desenvolvimento paralelas. Pense nelas como cópias do seu projeto onde você pode fazer alterações sem afetar a linha principal **(master/main)**.

A ilustração acima usa a analogia de uma linha do tempo de desenvolvimento de um site:

- **Main Branch (Ramo Principal)**: Representa a versão estável e "ao vivo" do seu projeto (geralmente chamada de master ou main). É a linha azul reta que nunca para.

- **Branch (Ramo de Funcionalidade)**: Quando você quer criar algo novo (como um "Blog" ou "Login"), você cria um desvio (a linha verde). Isso permite que você trabalhe e faça testes (os commits verdes) sem risco de quebrar o site principal.

- **Merge (Fusão)**: Quando a sua nova funcionalidade está pronta e testada, você realiza o Merge. É o momento em que o Git une o seu trabalho de volta à linha principal (a seta vermelha), integrando todas as novidades com segurança.

Esta visualização ajuda a entender por que usamos branches: para manter o desenvolvimento organizado e seguro, permitindo que várias pessoas trabalhem em funcionalidades diferentes ao mesmo tempo sem conflitos.


### 🌿 **Criando e Alternando entre Branches**

Como vimos na ilustração anterior, antes de iniciar qualquer modificação ou criar uma nova funcionalidade no projeto, o ideal é criar um ramo separado (Branch). Isso garante que o ramo principal (master ou main) permaneça estável e seguro.

Você pode criar e entrar em uma nova branch de duas formas: em um único comando (atalho) ou em duas etapas.

**⚡ Método 1: Criar e Entrar na Branch (Em um único comando)**<br>

Esta é a forma mais utilizada no dia a dia. Você avisa ao Git para criar o ramo e já mudar para ele imediatamente.

- **Forma Moderna (Recomendada):**<br>

O comando switch com a flag -c (de create) é a evolução do Git para tornar os comandos mais intuitivos.

    git switch -c nome-da-sua-branch

- **Forma Clássica:**<br>

O comando clássico utiliza o checkout com a flag -b (de branch). Você ainda o encontrará muito na internet e em projetos antigos.

    git checkout -b nome-da-sua-branch

**🐢 Método 2: Criar e Entrar (Em duas etapas)**<br>

Se você preferir fazer o processo passo a passo, a lógica se divide em: primeiro criar, depois "virar a chave" para entrar no ramo.

**Passo 1:** Criar a branch (ela é criada, mas você continua na branch atual):<br>

    git branch nome_da_sua_branch

**Passo 2:** Mudar para a branch recém-criada:<br>

    git switch nome_da_sua-branch

 ou o clássico:

    git checkout nome_da_sua_branch

<br>

🔍 **Como ter certeza de que mudei de branch?**

Após rodar qualquer um dos comandos acima, você pode validar sua posição de duas formas:

- Olhando o próprio terminal do Git Bash, que mudará o texto entre parênteses no final da linha (ex: de (master) para (nome_da_sua_branch)).

- Rodando o comando de status que aprendemos no início:

```
git status
```

O terminal vai mostrar algo assim:
<br>

```
On branch nome_da_sua_branch
nothing to commit, working tree clean
```
**A primeira linha exibirá:** On branch nome_da_sua_branch.

### 💡 **Dica de Nomenclatura**
Evite usar espaços ou caracteres especiais nos nomes das branches. Use sempre letras minúsculas e separe as palavras com hífen (-) ou underline (_).

🟢 **Bom:** nova-automacao ou correcao_login
<br>
🔴 **Evitar:** Nova Automacao ou correção/login!

### 🌿 **Renomear branch**

Às vezes, você pode cometer um erro ao digitar o nome da branch (como vimos na dica anterior) ou perceber que o nome não ficou ideal. O Git permite que você corrija isso de forma muito simples.

Para renomear uma branch na qual você **não** está atualmente, use o comando:

    git branch -m <nome_antigo> <nome_novo>

- **<nome_antigo>**: O nome atual da branch que você quer mudar.
- **<nome_novo>**: O novo nome desejado.

**Exemplo Prático:**

Suponha que você criou uma branch chamada "featue-login" por engano. Para corrigir, você digita:

    git branch -m featue-login feature-login

Caso você estiver na branch em que deseja mudar o nome, basta inserir somente o novo nome da branch:

    git branch -m <nome_novo>

### 🌿 **Excluindo branches**

Assim como a criação, a exclusão de branches também é uma operação comum no dia a dia de um desenvolvedor. Vejamos os cenários mais comuns:<br>
Quando uma funcionalidade é finalizada e incorporada à branch principal, ou quando uma branch é criada por engano, ela se torna desnecessária e pode ser excluída.

Para excluir uma branch, utilizamos o comando **git branch** com a flag **-d** (delete).

    git branch -d nome_da_branch

- **-d**: Flag que indica a exclusão da branch.
- **nome_da_branch**: Nome da branch que deseja excluir.

**Exemplo:**

    git branch -d nova-automacao

**Observação:** O Git só permitirá a exclusão de uma branch que não esteja em uso (ou seja, que você não esteja atualmente navegando nela) e que já tenha sido mesclada com a branch principal. Se tentar excluir uma branch não mesclada, o Git exibirá uma mensagem de erro.


### **Merge**

🤝 **Unindo os Trabalhos**

Depois que você criou uma branch separada, desenvolveu a nova funcionalidade e testou tudo localmente, chega o momento de trazer essas alterações de volta para a branch principal do projeto (master ou main). Esse processo de união é chamado de Merge (Fusão).


⚠️ **A Regra de Ouro do Merge**

Para fazer um merge sem erros, guarde esta regra: Você sempre deve se posicionar na branch que vai RECEBER as atualizações. Se você quer puxar as alterações da sua branch nova para a master, você precisa primeiro "entrar" na master.

🚀 **Passo a Passo Prático para Realizar o Merge**

Imagine o seguinte cenário: você terminou de trabalhar na branch chamada nova-automacao e agora quer enviar esse código para a master. 

Siga estes três passos:

**Passo 1:** Garanta que seu trabalho na branch atual está salvo
Antes de sair da sua branch, certifique-se de que fez o commit de tudo:
 
    git status
    # Deve exibir: "nothing to commit, working tree clean"


**Passo 2:** Mude para a branch de destino (a que vai receber as mudanças)

No nosso exemplo, queremos trazer as mudanças para a master:
 
    git switch master 

    ou 

    git checkout master

**Passo 3:** Execute o Merge puxando a branch nova
Agora que você está posicionado na master, dê a ordem para o Git puxar as alterações da branch de desenvolvimento:
 
    git merge nome_da_sua_branch


As alterações da sua branch são trazidas para a linha principal.

⚙️ **O que acontece por trás dos panos?**

Dependendo do histórico do seu projeto, o Git pode realizar o merge de duas formas automáticas:

- **Fast-Forward (Avanço Rápido):** Acontece se a branch master não sofreu nenhuma alteração enquanto você trabalhava na branch separada. O Git simplesmente "empurra" o ponteiro da master para a frente, igualando-a ao seu último commit. É o merge mais limpo e rápido.

- **Merge Commit (Commit de Fusão):** Se outra pessoa tiver alterado a master enquanto você trabalhava na sua branch, o Git unirá as duas linhas do tempo criando um commit especial automaticamente (chamado Merge commit), juntando o histórico de ambas.

💡 **Dica de Organização: Limpando a casa**

Depois que o merge foi concluído com sucesso, aquela branch de desenvolvimento (nova-automacao) perde a utilidade, pois todo o código dela já está salvo na linha principal. Para manter seu repositório organizado, você pode deletá-la com o comando:

    git branch -d nome_da_sua_branch

<br>
<br>

---


# ☁️ **Entrando na Nuvem: O GitHub e o Repositório Remoto**

Até agora, todas as mágicas, commits e branches que fizemos aconteceram apenas dentro da sua máquina (no repositório local). Se o seu computador quebrar, você perde o projeto.

O GitHub entra justamente para resolver isso: ele serve como um servidor seguro na nuvem (repositório remoto) onde você pode guardar o seu histórico, fazer backups e compartilhar seu código com outras pessoas.

O primeiro passo para conectar o seu computador à nuvem é criar um repositório vazio no GitHub.

### 🔨 **Passo 1: Criando o Repositório no site do GitHub**
Acesse o site do GitHub e faça login na sua conta.
No canto superior direito, clique no botão + (mais) e selecione New repository (Novo repositório).
Preencha as informações básicas:

- **Repository name**: Digite o nome do seu projeto (ex: meu-projeto-automacao).
- **Description (Opcional)**: Uma breve frase explicando o que o projeto faz.
- **Public / Private**: Escolha se qualquer pessoa pode ver seu código (Público) ou se apenas você e convidados terão acesso (Privado).

⚠️ **ATENÇÃO (Regra de Ouro)**: Como você já tem um projeto iniciado na sua máquina, NÃO marque nenhuma das opções de inicialização (Add a README file, Add .gitignore ou Choose a license). Deixe todas desmarcadas para o repositório nascer completamente vazio.

Clique no botão verde Create repository.

### 🔗 **Passo 2: Conectando o seu Computador ao GitHub**

Assim que o repositório for criado, o GitHub exibirá uma tela com vários comandos. O próprio GitHub te dá a cola de como conectar a sua pasta local à nuvem.

Procure pela seção chamada **"…or push an existing repository from the command line"** (ou empurrar um repositório existente a partir da linha de comando). No seu Git Bash, dentro da pasta do seu projeto, você executará os seguintes comandos:

1. **Vincular o endereço da nuvem ao seu terminal:**
Este comando cria um apelido chamado **origin** (Diretório Remoto Principal) que aponta diretamente para o link do seu projeto no GitHub.

    ```
    git remote add origin https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Definir o nome correto da branch principal:
O GitHub adota por padrão o nome main para a branch principal. Se o seu Git local ainda estiver usando o termo antigo master, este comando renomeia ela para main para evitar conflitos:

    ```
    git branch -M main
    ```

### 🚀 **Passo 3: Subindo o código pela primeira vez (git push)**
Agora que o computador e a nuvem estão conectados, você vai "empurrar" (fazer o upload) dos seus commits locais para o GitHub utilizando o comando git push:

    git push -u origin main

### 🔍 **O que significa esse comando?**

- **git push**: O comando de envio/upload.
- **-u**: Abreviação de set-upstream. Você só precisa usar essa flag na primeira vez que envia o código. Ela diz ao Git local: "memorize que a branch main daqui deve sempre se sincronizar com a branch main do origin (GitHub)".
- **origin main**: Indica o destino (origin, que é o link do GitHub) e a branch que você está enviando (main).

🔐 **Nota de Autenticação**: Na primeira vez que rodar o git push, o Git poderá abrir uma janela no seu navegador pedindo autorização para o terminal acessar a sua conta do GitHub. Basta clicar em "Authorize" e confirmar com sua senha.

🔄 **Os próximos envios do dia a dia**

Nas próximas vezes que você fizer alterações no código, fizer novos commits e quiser atualizar o GitHub, o processo será muito mais simples. Você não precisará refazer as configurações, bastará digitar:

    git push

O Git já lembrará do caminho e atualizará o site instantaneamente!


#### **Caso não tenha efetuado os comandos GIT localmente (Realizado commit local), mas deseja criar um novo repositório utilizando a linha de comando (Git Bash), faça o seguinte:**

1. No site do GitHub, crie um repositório vazio.
2. No Git Bash, na pasta do projeto, execute os comandos:
    
    ```
    git init
    git add .
    git commit -m "Mensagem inicial"
    git remote add origin https://github.com/seu-usuario/seu-repositorio.git
    git branch -M main
    git push -u origin main
    ```

<br>

### 🏢 **Trabalhando em Equipe: Clonando e Atualizando Projetos**

Quando você entra em uma empresa ou passa a colaborar em um projeto que já existe no GitHub, você não precisa iniciar um repositório do zero. O fluxo de trabalho padrão consiste em trazer esse projeto para a sua máquina e mantê-lo sincronizado com as alterações do restante do time.

📥 **1. Baixando o projeto pela primeira vez: O git clone**

Para fazer o download completo de um repositório do GitHub (incluindo todos os arquivos, branches e o histórico de commits) para o seu computador, utilizamos o comando git clone.

Como fazer:
No GitHub, acesse a página do projeto da empresa.

Clique no botão verde Code e copie a URL que aparece (focando na aba HTTPS).

No seu Git Bash, navegue até a pasta onde você costuma guardar seus projetos (ex: cd Documents/Projetos) e digite:

    git clone https://github.com/empresa/projeto-da-equipe.git

📂 **O que acontece depois?**

O Git criará automaticamente uma nova pasta com o nome do projeto dentro do diretório onde você estava. Não se esqueça de entrar na pasta do projeto usando o comando cd nome-do-projeto antes de começar a trabalhar ou rodar outros comandos!

🔄 **2. A Rotina do Dia a Dia: Checar e Atualizar**

Depois de clonar, você criará sua **branch** e fará suas alterações e **commits** locais normalmente. Porém, antes de enviar o seu trabalho para o GitHub, criar a nova **branch** ou iniciar uma nova tarefa, você precisa garantir que o seu código local está alinhado com o que a equipe produziu nesse meio tempo.

Se você tentar enviar algo e o repositório do GitHub tiver **commits** novos que você não tem na sua máquina, o Git vai recusar o seu envio.

### **Passo A: Como checar se o GitHub mudou?**

Para verificar se existem novidades na nuvem sem misturar nada ao seu código ainda, o comando correto é o git fetch (e não o **git log** direto, pois o log local só conhece o que já está no seu computador).

    git fetch origin

Esse comando vai até o GitHub (origin), olha o que tem de novo lá e atualiza o histórico do seu terminal, mas deixa seus arquivos intactos.

Agora sim, se você rodar o comando abaixo, poderá comparar visualmente onde está o seu projeto local em relação ao GitHub:

    git status

Se a equipe tiver feito commits na nuvem, o terminal exibirá uma mensagem como:

👉 "Your branch is behind 'origin/main' by 3 commits..." (Sua branch está atrás da nuvem por 3 commits).

### **Passo B: Trazendo as novidades para a sua máquina (git pull)**

Se o status apontou que existem atualizações pendentes, você precisa puxar essas alterações para o seu computador para sincronizar o projeto. Utilize o comando:

    git pull origin main

Esse comando funciona de forma semelhante ao git fetch, mas ele executa uma ação extra: ele mescla (faz o **merge**) automaticamente as alterações que vieram do GitHub com o código da sua branch atual. É a forma mais rápida de colocar sua máquina em sincronia com a equipe.

🔍 **Entendendo o comando:**

O **git pull** funciona como uma combinação de dois comandos: ele busca as novidades na nuvem (**git fetch**) e já realiza a fusão delas automaticamente na sua branch atual (**git merge**).


### ⚠️ **Atenção: Conflitos de Merge (Merge Conflicts)**

E se você e um colega mexeram na mesma linha do mesmo arquivo ao mesmo tempo? O Git não consegue decidir sozinho qual versão manter.

Nesse caso, o **git pull** vai parar e avisar você sobre um **"Merge Conflict"**. O arquivo ficará "marcado" com setas especiais (como `<<<<<<< HEAD` e `>>>>>>>`) mostrando as versões de cada um.

**Como resolver?**
1. Abra o arquivo no editor de código.
2. Procure pelos marcadores de conflito.
3. Edite o trecho para deixar o código como você deseja (escolhendo uma versão ou misturando partes de ambas).
4. Remova as setas e linhas de marcação do Git.
5. Salve o arquivo.
6. Finalize adicionando e commitando a resolução:
   ```bash
   git add nome-do-arquivo-corrigido.js
   git commit -m "Resolução de conflito no arquivo X"
   ```

🎉 **Parabéns!** Agora você entende o ciclo completo de trabalho remoto: desde clonar um projeto até subir suas alterações com segurança.


### 💡 **Checklist Diário do Desenvolvedor**

- Chegou para trabalhar? Dê um **git pull** para começar o dia com o código mais recente da equipe.

- Terminou sua tarefa local? Dê um **git fetch** e um **git status** para garantir que ninguém mexeu na branch principal antes de você subir as suas alterações.

# **Trabalhando com Pull Requests (PR) e Merge Requests (MR)**

O Pull Request (PR) é uma funcionalidade que permite que você solicite a inclusão das alterações que você fez em uma branch para outra branch. É uma forma de solicitar que o seu código seja revisado por outros desenvolvedores antes de ser mesclado ao código principal.

Para isso você deve seguir os passos abaixo:

1. Crie uma nova branch:
    ```bash
    git checkout -b nome-da-nova-branch
    ```
2. Faça as alterações desejadas no código.
3. Adicione e commite as alterações:
    ```bash
    git add .
    git commit -m "Mensagem descritiva sobre as alterações"
    ```
4. Suba a nova branch para o GitHub:
    ```bash
    git push -u origin nome-da-nova-branch
    ```

A partir daqui você não trabalhara mais com o terminal, mas sim com o site do **GitHub**.

5. Acesse o **GitHub** e clique no botão **"New Pull Request"** (Novo Pull Request).
6. Selecione a **branch** de origem e a **branch** de destino.
7. Adicione uma descrição do seu Pull Request e clique em **"Create Pull Request"** (Criar Pull Request).

Pronto, agora seu **PR (Pull Request)** foi enviado para revisão. Se alguém pedir alterações, você poderá fazer as alterações, commitar e enviar novamente. Caso contrário, alguém da equipe irá aprovar e mesclar o seu PR.
<br>
Normalmente são desenvolvedores senior que realizam a analise e a aprovação dos PR's.

Caso você seja um desenvolvedor senior e precise aprovar um PR, você deve seguir os passos a seguir:

1. Acesse o **GitHub** e clique no botão **"Pull Requests"** (Pull Requests).
2. Clique no **PR** que você deseja aprovar.
3. Clique no botão **"Approve"** (Aprovar).

<br>
<br>


# **🍴 O que é o Fork e para que serve?**

Imagine que a sua empresa tem um projeto principal muito importante. Em vez de dar acesso direto para que qualquer desenvolvedor altere esse código principal (o que poderia causar acidentes e quebrar o sistema), o GitHub permite que você tire uma cópia idêntica e independente desse projeto para a sua própria conta de usuário.

Essa ação de clonar um repositório de outra pessoa ou empresa diretamente para a sua conta do GitHub é chamada de Fork (Bifurcação).

**🔍 Qual é a diferença entre Fork e Clone?**
<br>
É muito comum confundir esses dois conceitos, mas eles atuam em camadas diferentes:

- **git clone (Nuvem ➔ Computador)**: Copia os arquivos do GitHub diretamente para a sua máquina física.
- **Fork (Nuvem ➔ Nuvem)**: Copia o projeto de uma conta do GitHub (ex: github.com/empresa/projeto) para a sua conta do GitHub (ex: github.com/seu-usuario/projeto). Ele cria uma cópia na nuvem.

**🚀 O Fluxo de Trabalho com Fork**
<br>
Trabalhar com Fork introduz um passo a mais no desenvolvimento seguro. O fluxo padrão na maioria das empresas segue estes passos:

- **Fazer o Fork**: Você entra no repositório da empresa pelo site do GitHub e clica no botão Fork (no canto superior direito). Agora você tem o projeto na sua conta.

- **Clonar o SEU Fork**: Você faz o git clone do link da sua cópia para o seu computador.

- **Desenvolver**: Você cria sua branch, faz alterações e dá o git push. Esse push vai para o seu repositório no GitHub (sua cópia segura).

- **Pedir para integrar (Pull Request)**: Quando o seu trabalho estiver pronto e você quiser enviar para o projeto principal da empresa, você entra no GitHub e abre um Pull Request (PR). O gerente do projeto vai analisar o seu código e, se estiver tudo certo, ele aceitará a sua alteração.

**💡 Por que as empresas usam o Fork?**
Segurança Absoluta: O repositório principal fica protegido. Ninguém consegue estragar a versão oficial do software sem passar pela aprovação de um revisor.

Organização: Permite que desenvolvedores externos ou novos funcionários testem ideias livremente em suas próprias cópias sem poluir o histórico de commits da empresa.


# **Agora vamos falar de Pull Request usando Fork**

**🔀 Como funciona o Pull Request (PR) usando Fork?**
<br>
Quando trabalhamos com Branches dentro do mesmo repositório, o **Pull Request** une a **sua-branch** com a **main** no mesmo lugar.

No caso do **Fork**, você criou um repositório totalmente novo na sua conta **(ex: seu-usuario/projeto)**. Você faz alterações nele, faz os **commits** e dá o **git push**. O código vai para o seu GitHub.

Mas como enviar de volta para a empresa? Através de um Pull Request entre repositórios (Cross-Repository Pull Request).

**🔄 O Passo a Passo na Interface do GitHub**
<br>
Você não faz esse Pull Request pelo terminal (Git Bash), você faz diretamente pela interface web do GitHub:

Acesse o **SEU repositório no GitHub (o seu Fork, ex: github.com/seu-usuario/projeto)**.

Logo na página inicial do seu projeto, o GitHub exibirá um aviso cinza bem discreto dizendo:
```
“This branch is 3 commits ahead of empresa:main” (Esta branch está 3 commits à frente do projeto da empresa).
```
Ao lado desse aviso, haverá um botão chamado **Contribute (Contribuir)** ou **Open Pull Request**. 👉 Clique nele!

O GitHub abrirá a tela de comparação. É aqui que a mágica acontece. Ele mostrará quatro campos na parte superior:

```
base repository: empresa/projeto ◄ base: main

── compara com ──

head repository: seu-usuario/projeto ◄ compare: sua-branch-de-trabalho
```

**O que isso significa?**

**Você está dizendo ao GitHub:** "Por favor, pegue as alterações da minha branch que está no meu repositório pessoal e peça autorização para injetá-las na branch main do repositório oficial da empresa".

Clique no botão verde Create Pull Request, escreva o título, explique o que você fez e confirme.

**🛡️ O que acontece depois?**

O seu **Pull Request** sairá da sua conta e vai aparecer na aba **"Pull Requests"** lá no repositório da empresa.

O gestor ou o revisor do código (Code Reviewer) da empresa receberá uma notificação. Ele poderá:

- Olhar linha por linha o que você alterou.
- Fazer comentários pedindo ajustes.

Se estiver tudo perfeito, ele clicará em Merge, e o seu código finalmente entrará no repositório principal da empresa.

**📝 Resumo para fixar:**

**Pull Request comum:** Une Branch A ➔ Branch B (Dentro do mesmo repositório).

**Pull Request com Fork:** Une **Repositório Pessoal/Branch A** ➔ **Repositório da Empresa/Branch Principal**. O GitHub gerencia essa ponte entre as duas contas automaticamente porque ele sabe que o seu projeto nasceu a partir de um Fork do deles.

