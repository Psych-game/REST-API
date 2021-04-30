curl -X POST -F "username=coderofworlds" -F "email=a@a.a" -F "password=boza" \
    http://127.0.0.1:5000/register

curl -X POST -F "username=coderofworlds1" -F "email=a@a." -F "password=boza" \
    http://127.0.0.1:5000/register