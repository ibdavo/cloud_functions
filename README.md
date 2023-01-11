# README



#Pre-installation requirements
    -[] gcloud CLI:  https://cloud.google.com/sdk/docs/install
    
    Emulators
        -[] Cloud Functions Emulator:  https://cloud.google.com/functions/docs/emulator
        -[] Cloud Pub/Sub Emulator:  https://cloud.google.com/pubsub/docs/emulator
            The pubsub emulator requires Java JRE 7+ to be installed. 
                curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u112-b15/jre-8u112-macosx-x64.dmg > jre-8u112-macosx-x64.dmg
                curl -v -j -k -L -H "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u351-b15/jre-8u351-macosx-x64.dmg > jre-8u351-macosx-x64.dmg
        -[] 

## Start emulator
        $ gcloud beta emulators pubsub start --project=testproj --host-port='localhost:7001'
        You need the [pubsub-emulator] component to use the Google Cloud
        Pub/Sub emulator.


        Your current Google Cloud CLI version is: 410.0.0
        Installing components from version: 410.0.0

        ┌─────────────────────────────────────────────┐
        │     These components will be installed.     │
        ├────────────────────────┬─────────┬──────────┤
        │          Name          │ Version │   Size   │
        ├────────────────────────┼─────────┼──────────┤
        │ Cloud Pub/Sub Emulator │   0.7.1 │ 62.4 MiB │
        └────────────────────────┴─────────┴──────────┘

        For the latest full release notes, please visit:
        https://cloud.google.com/sdk/release_notes

        Do you want to continue (Y/n)?