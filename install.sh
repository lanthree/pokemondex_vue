#!/bin/bash
npm run build
rm -r utool_dist
mkdir utool_dist
cp utools/* utool_dist/
cp -r dist/* utool_dist/
rm utool_dist/js/*.js.map