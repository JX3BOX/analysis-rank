1. 总览：根据当前活动全部数据生成
a.提交成绩总数，各个服的提交数（可看出活跃度）
b.根据status排查出来的外挂或各种代打情况比例

2. 100强成绩分析
a.每个boss的100强各个区服的总数，求出最多的前3和垫底的2

3. 100强职业分析：
a.职业比例
b.心法比例
c.奶妈各个比例
d.MT各个比例
e.DPS各心法比例
f.外攻内攻比例

## 项目结构
- csv: 原数据
    - event_id 活动编号
        - 源csv文件
- json_raw: 根据csv原数据导出的json格式数据 格式：活动编号_成就id
- analytics: 统计文件夹
    - script: 每一个统计项目的单独py脚本
    - event${i}: 活动编号
        - 每一个统计项目的单独文件夹
            - 每一个boss（成就id）
- stats: 最终生成的统计文件
    - event${i}.json 以活动编号为标注的最终数据文件

### 统计项目内容
- bar_server_all: 每个区服各有多少各团队
- bar_server_top10: 前十名的团队的区服分布
- pie_dps_xf_ratio dps心法比例
- pie_hps_count 奶妈数量
- pie_hps_xf_ratio 奶妈各心法比例
- pie_leader_type_ratio 团长职业类型分布
- pie_neiwaigong_ratio 外功内功比例
- pie_school_ratio 门派比例
- pie_tank_count t数量
- pie_tank_xf_ratio t各心法比例
- pie_xf_ratio 各心法比例

