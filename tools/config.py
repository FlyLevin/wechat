#coding:utf8

# For the app group change func, correspond to the app_group table

NOT_REGISTERED_GROUPID = 1
REGISTERED_GROUPID = 2

# For the proposal table change, correspond to the different proposal stage

proposal_stages = {
    'PROPOSAL_STAGE_PENDING': 0,
    'PROPOSAL_STAGE_DISCUSS': 1,
    'PROPOSAL_STAGE_VOTE': 2,
    'PROPOSAL_STAGE_FREEZE': 3,
    'PROPOSAL_STAGE_DONE': 4,
    'PROPOSAL_STAGE_CLOSE': 5
}

proposal_stage_name = ['']*len(proposal_stages)

# prepare the stage name for UI showing
for i in range(len(proposal_stages)):
    proposal_stage_name[proposal_stages[proposal_stages.keys()[i]]] = proposal_stages.keys()[i].split('_')[2]


# wechat error message UI, message information showing

ERROR_NOTSUBSCRIBE_OR_ID_EXIST = "该身份证号码已被实名或输入有误 请重新输入"
ERROR_NOTREGISTERED_USER = "非认证用户 请首先实名认证"
ERROR_USER_ALREADY_SECONDED = "你已经附议 请勿重复提交"
ERROR_USER_ALREADY_SECONDED = "你已经投票 请勿重复提交"
ERROR_USERID_PARAMETER = "参数错误 请求处理失败 请重新提交"
