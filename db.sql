create table admin (
	id_admin integer generated always as identity primary key,
	username_admin varchar(250) NOT NULL,
	email_admin  varchar(100) UNIQUE NOT NULL,
	adresse_admin varchar(100) NOT NULL,
	numero_tel_admin varchar(9) NOT NULL
);

create table groupe_users (
	id_groupe_users integer generated always as identity primary key,
	id_admin INTEGER NOT NULL, 
	date_creation_groupe TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT FK_ADMIN_GROUPE
		FOREIGN KEY (id_admin)
		references admin (id_admin)
		on delete cascade 
		on update cascade
);

create table users (
	id_users integer generated always as identity primary key,
	username varchar(250) NOT NULL,
	email_users varchar(100) UNIQUE NOT NULL,
	adresse_users varchar(100) NOT NULL,
	numero_tel_users varchar(9) NOT NULL,
	id_admin INTEGER NOT NULL, 
	id_groupe_users INTEGER,
	date_creation_users TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT FK_ADMIN_USERS
		FOREIGN KEY (id_admin)
		references admin (id_admin)
		on delete cascade 
		on update cascade,
	CONSTRAINT FK_GROUPE_USERS
		FOREIGN KEY (id_groupe_users)
		references groupe_users (id_groupe_users)
		on delete set null 
		on update cascade
);

create table prompt (
	id_prompt integer generated always as identity primary key,
	date_creation_prompt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	description varchar(255) NOT NULL,
	status varchar(255),
	date_modification TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	id_admin integer,
	CONSTRAINT FK_ADMIN_PROMPT
		FOREIGN KEY (id_admin)
		references admin (id_admin)
		on delete cascade 
		on update cascade
);

create table vote (
	id_vote integer generated always as identity primary key,
	id_users integer NOT NULL,
	id_prompt integer,
	poids_vote integer,
	date_creation_vote TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT FK_USER_VOTE
		FOREIGN KEY (id_users)
		references users (id_users)
		on delete cascade 
		on update cascade,
	CONSTRAINT FK_PROMPT_VOTE
		FOREIGN KEY (id_prompt)
		references prompt (id_prompt)
		on delete cascade 
		on update cascade
);

create table note (
	id_note integer generated always as identity primary key,
	id_users integer NOT NULL,
	id_prompt integer,
	poids_note integer,
	date_creation_note TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT FK_USER_NOTE
		FOREIGN KEY (id_users)
		references users (id_users)
		on delete cascade 
		on update cascade,
	CONSTRAINT FK_PROMPT_NOTE
		FOREIGN KEY (id_prompt)
		references prompt (id_prompt)
		on delete cascade 
		on update cascade
);

create table vente (
	id_vente integer generated always as identity primary key,
	id_session_invite integer,
	id_prompt integer,
	date_vente TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT FK_PROMPT_VENTE
		FOREIGN KEY (id_prompt)
		references prompts (id_prompt)
		on delete cascade 
		on update cascade
);

