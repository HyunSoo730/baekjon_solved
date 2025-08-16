# p_id null이면 ROOT
# p_id에 등장하면 INNER 
# p_id에 없으면 LEAF
WITH tempA as (
    select distinct p_id 
    from Tree
)
select 
    id,
    CASE 
        WHEN p_id is null then 'Root'
        WHEN id in (select p_id from tempA) then 'Inner'
        else 'Leaf'
    END AS type
from Tree;