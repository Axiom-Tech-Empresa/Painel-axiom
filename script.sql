-- Habilita o suporte a chaves estrangeiras no SQLite (importante!)
PRAGMA foreign_keys = ON;

-- -----------------------------------------------------
-- Tabela 1: Usuarios
-- -----------------------------------------------------
CREATE TABLE Usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha_hash TEXT NOT NULL,
    data_criacao TEXT DEFAULT (DATETIME('now')),
    is_admin INTEGER NOT NULL DEFAULT 0
);

-- -----------------------------------------------------
-- Tabela 2: Sistemas
-- -----------------------------------------------------
CREATE TABLE Sistemas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    id_criador INTEGER NOT NULL,
    data_criacao TEXT DEFAULT (DATETIME('now')),
    
    FOREIGN KEY (id_criador) REFERENCES Usuarios (id)
);

-- -----------------------------------------------------
-- Tabela 3: SistemasUsuarios (Tabela de Junção)
-- -----------------------------------------------------
CREATE TABLE SistemasUsuarios (
    id_sistema INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL,
    
    status_ativo INTEGER NOT NULL DEFAULT 1, 
    data_vinculo TEXT DEFAULT (DATETIME('now')),
    
    -- [NOVA COLUNA]
    -- Armazena a data/hora que o acesso expira.
    -- Se for NULL, o acesso não expira.
    data_expira TEXT DEFAULT NULL,
    
    -- Chaves estrangeiras
    FOREIGN KEY (id_sistema) REFERENCES Sistemas (id),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios (id),
    
    -- Chave primária composta
    PRIMARY KEY (id_sistema, id_usuario)
);
```eof

---