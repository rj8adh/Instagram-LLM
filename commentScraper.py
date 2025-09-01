from dotenv import load_dotenv
from apify_client import ApifyClientAsync
from datetime import datetime
import asyncio
import json
import os

load_dotenv()

apifyKey = os.getenv("BACKUP_KEY")
# print(apifyKey)

async def main() -> None:
    apify_client = ApifyClientAsync(apifyKey)
    allComments = []

    # Start an Actor and wait for it to finish.
    actor_client = apify_client.actor('apify/instagram-comment-scraper')

    with open('allReels.json', 'r') as f:
        allReelData = json.load(f)

    allReelData = [data for data in allReelData if data['Sender'] != 'Samved'] # Remove Samved's comments lmao
    # print(allReelData)
    allUrls = []
    counter = 0
    for reelData in allReelData:
        reel = reelData['Reel']
        if reel not in allUrls:
            allUrls.append(reel)
        else:
            counter+=1
    print(counter)

    # print(len(allUrls))

    input_data = {
    "directUrls": allUrls[500:],
    "includeNestedComments": False,
    "isNewestComments": False,
    "resultsLimit": 15
    }

    run_result = await actor_client.call(run_input=input_data, timeout_secs=60)

    if run_result is None:
        print('Actor run failed.')
        return
    
    # print(run_result)

    # Fetch and print Actor results from the run's dataset (if there are any)
    async for item in apify_client.dataset(run_result["defaultDatasetId"]).iterate_items():
        print(item)
        allComments.append(item)

    print(type(run_result))
    print(len(run_result))

    with open(f'{str(datetime.now().strftime("Comments_%Y-%m-%d_%H-%M-%S"))}.json', 'w') as f:
        json.dump(allComments, f, indent=4)

if __name__ == '__main__':
    asyncio.run(main())