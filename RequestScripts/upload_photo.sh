#!/bin/bash

# Upload a photo 

# curl -S localhost:8000/api/photo/ -F "image=@/home/vfdev/Downloads/wastes.jpg;filename=uploaded_file_123.jpg;type=image/*" -H 'Authorization: Token 20bc9187c436e47ce7d2caa7f896a40dd91782ee' > log.html

# curl -S localhost:8000/api/photo/ -F "image=@/Users/vfomin/Downloads/forestWaste2.jpg;filename=uploaded_file_777.jpg;type=image/*" -H 'Authorization: Token 20bc9187c436e47ce7d2caa7f896a40dd91782ee'
curl -S localhost:8000/api/photo/ -F "image=@/Users/vfomin/Downloads/forestWaste2.jpg;filename=uploaded_file_234.jpg;type=image/*" -H 'Authorization: Token c10e32d8a1e5076a0a5fef19a711db7fa407500a'

echo


