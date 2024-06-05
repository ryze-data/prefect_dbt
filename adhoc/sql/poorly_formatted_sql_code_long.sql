SELECT
 DISTINCT
  a.id AS alpha_id,
  b.id AS beta_id,
  g.id AS gamma_id,
  d.id AS delta_id,
  sum(d.value) AS total
FROM
  alphas AS a,
  betas AS b,
  (
SELECT
        DISTINCT
beta_id FROM
deltas UNION
SELECT
        DISTINCT
beta_id FROM
epsilons
  ) AS c
INNER JOIN gammas AS g ON g.id = a.beta_id
INNER JOIN (
SELECT
 child_id, count(*) as num
FROM alphas
WHERE
 visible = TRUE
GROUP BY
    child_id
) AS ap ON
 ap.child_id = a.id AND ap.num >= g.min_parents
LEFT OUTER JOIN deltas AS d ON d.id = g.delta_id
WHERE
 a.visible = TRUE AND b.id = a.beta_id AND c.beta_id = a.beta_id
GROUP BY alpha_id, beta_id,
gamma_id,
delta_id
      HAVING
count(*) > 1 AND
total < 100
      ORDER BY
