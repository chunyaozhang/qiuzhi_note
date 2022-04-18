-- 用户留存题
select date,round(count(distinct d.user_id)/count(distinct c.user_id),3) as p
from(
	select a.date,b.user_id
	from (
		-- 1. 取所有的日期
		select distinct l1.date
     	from login as l1
     	) as a
     left join (
     	-- 2. 取每个用户最早的登录时间
     	select user_id, min(date) as m_date
     	from login as l2
     	group by user_id
     	) as b
      on a.date = b.m_date
      ) as c
left join(
	-- 3. 取登录时间相差1天的
	select distinct l3.user_id
	from login l3,login l4
	where l3.user_id =l4.user_id
	and date_add(l3.date,interval 1 day)=l4.date
	) as d
on c.user_id = d.user_id
group by date


-- 查询用户的最长连续活跃天数
