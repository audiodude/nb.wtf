<?php
namespace NBWTF;

use GuzzleHttp\Client;
use GuzzleHttp\Psr7\Request;

use MediaWiki\Title\Title;

class Hooks
{
  public static function onPageSaveComplete(
    $wikiPage,
  ) {
    if (!$wikiPage->getTitle()->equals(Title::newFromText('Nb.wtf'))) {
      return;
    }

    // Fire and forget a GET request to the nb.wtf API.
    $client = new Client();
    $request = new Request('GET', 'https://nb.wtf/api/v1/on_update');
    $response = $client->send($request);
  }
}