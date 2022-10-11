mkdir /etc/tempura
touch /etc/tempura/tempura.conf

printf "[DEFAULT]
nologin=no

[common]
db_host=127.0.0.1
db_port=2715
db_user=admin
db_pass=tempura
" > /etc/tempura/tempura.conf

printf "Installation Complete!\n"

# create user and group for TempuraDB