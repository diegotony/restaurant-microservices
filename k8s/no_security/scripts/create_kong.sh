kubectl apply -f kong/kong.yml
kubectl apply -f kong/paths.yml
# kubectl apply -f kong/plugins.yml

# kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
# kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
# kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
# kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
# kubectl patch svc billing-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'

# kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
# kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
# kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
# kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
# kubectl patch svc client-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'

# kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
# kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
# kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
# kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
# kubectl patch svc fee-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'


# kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "rl-by-ip\n"}}}'
# kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-id\n"}}}'
# kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "cors\n"}}}'
# kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "request-termination\n"}}}'
# kubectl patch svc orden-api -p '{"metadata":{"annotations":{"plugins.konghq.com": "bot-detection\n"}}}'


#kubectl create configmap kongconfig --from-file=gateway/conf.d
#kubectl apply -f gateway/gateway-deploy-ser.yaml