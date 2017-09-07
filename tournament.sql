-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table players (
    id serial primary key,
    full_name text
);

create table matches(
    id serial primary key,
    winner int references players(id),
    loser int references players(id)
);

create view player_standing as
select
p.id,
p.full_name,
(select count(*) from matches where matches.winner = p.id) as won,
(select count(*) from matches where p.id = matches.winner or p.id = matches.loser) as played
from players p
group by p.id
order by won;