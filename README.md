# hop_snap


## Generate Messages
Messages can be generated while in the hop_snap directory with:
`python generate.py`

## Subscribe to Hop Channels
You must also subscribe to the two hop channels:
`hop subscribe --no-auth $TIMEDATA_TOPIC --persist`
`hop subscribe --no-auth $POST_TOPIC --persist`

## Combining Data
Start combining data with:
`snap sntest2.yml -n node_combine`
