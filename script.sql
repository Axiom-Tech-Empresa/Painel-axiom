-- Habilita o suporte a chaves estrangeiras no SQLite (importante!)
PRAGMA foreign_keys = ON;

-- -----------------------------------------------------
-- Tabela 1: Usuarios
-- Armazena os perfis de usuários.
-- -----------------------------------------------------
CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL,
    data_criacao TEXT DEFAULT (DATETIME('now'))
);

-- -----------------------------------------------------
-- Tabela 2: Sistemas
-- Armazena os sistemas/produtos que podem ser criados.
-- -----------------------------------------------------
CREATE TABLE Sistemas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    id_criador INTEGER NOT NULL,
    data_criacao TEXT DEFAULT (DATETIME('now')),
    
    -- Chave estrangeira que aponta para o usuário que criou o sistema
    FOREIGN KEY (id_criador) REFERENCES Usuarios (id)
);

-- -----------------------------------------------------
-- Tabela 3: SistemasUsuarios (Tabela de Junção)
-- Vincula usuários a sistemas e define seu status (ativo/inativo).
-- -----------------------------------------------------
CREATE TABLE SistemasUsuarios (
    id_sistema INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    
    -- 1 para Ativo (true), 0 para Inativo (false).
    -- Define 1 (Ativo) como padrão ao criar o vínculo.
    status_ativo INTEGER NOT NULL DEFAULT 1, 
    
    data_vinculo TEXT DEFAULT (DATETIME('now')),
    
    -- Chaves estrangeiras
    FOREIGN KEY (id_sistema) REFERENCES Sistemas (id),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios (id),
    
    -- Chave primária composta: garante que um usuário só pode 
    -- estar vinculado a um sistema uma única vez.
    PRIMARY KEY (id_sistema, id_usuario)
);