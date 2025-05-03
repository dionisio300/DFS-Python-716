-- 1. Alunos e seus detalhes
SELECT a.nome, d.endereco, d.telefone 
FROM alunos a
JOIN detalhes_alunos d ON a.id = d.id;

-- 2. Disciplinas e seus cursos
SELECT d.nome AS disciplina, c.nome AS curso
FROM disciplinas d
JOIN cursos c ON d.curso_id = c.id;

-- 3. Alunos matriculados e suas disciplinas
SELECT a.nome AS aluno, d.nome AS disciplina
FROM matriculas m
JOIN alunos a ON m.aluno_id = a.id
JOIN disciplinas d ON m.disciplina_id = d.id;

-- 4. Disciplinas com mais de 2 alunos matriculados
SELECT d.nome, COUNT(m.aluno_id) AS qtd_alunos
FROM matriculas m
JOIN disciplinas d ON m.disciplina_id = d.id
GROUP BY d.nome
HAVING COUNT(m.aluno_id) > 2;
