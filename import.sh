#Configure specifics for your environment
echo "Setting up Python Requirements"
pip3 install -r requirements.txt
HOST="couchbase://192.168.5.54"
USER="Administrator"
PWD="password123"
CBIMPORTPATH="/Applications/cbcli/bin/"
RECORDS=1000

export PATH="$PATH:$CBIMPORTPATH"

rm ./package_data.json
python3 generator.py -r $RECORDS

cbimport json \
-format lines \
-d ./package_data.json \
-b operations \
-g %tracking_id% \
--scope-collection-exp 'shipping.tracking' \
-c $HOST \
-u $USER \
-p $PWD
