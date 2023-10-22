# import asyncio
# from websockets.server import serve

# async def echo(websocket):
#     async for message in websocket:
#         await websocket.send(message)

# async def main():
#     async with serve(echo, "localhost", 8765, origins=["http://localhost"]):
#         await asyncio.Future()

# asyncio.run(main())

# PATH = 'C:/Users/wisle/Downloads/teste/'
# files = os.listdir(PATH)
# file_num = len(files)
# status = ''

# def watching():
#     for file in files:
#         FILE_PATH = os.path.join(PATH, file)
        
#         if os.path.isfile(FILE_PATH):
#             print('Existe OS aberta')
#             status = 'Existe OS aberta'
#             break
#         else:
#             print('Nenhuma OS aberta')
#             status = 'Nenhuma OS aberta'

#     if file_num == 0:
#         data_status = [
#             {
#                 'status': status,
#                 'num_os': 0
#             }
#         ]
#         return data_status
#     else:
#         data_status = [
#             {
#                 'status': status,
#                 'num_os': file_num
#             }
#         ]
#     return data_status

# @app.route('/changes', methods=['GET'])
# def get_changes():
#     monitoring = watching()
#     return jsonify(monitoring)