from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pergunta, Resultado
from .serializers import PerguntaSerializer, ResultadoSerializer

#retorna até 5 perguntas aleatórias do nível selecionado
@api_view(['GET'])
def listar_perguntas(request, nivel):
    perguntas = Pergunta.objects.filter(nivel=nivel).order_by('?')[:5]
    serializer = PerguntaSerializer(perguntas, many=True)
    return Response(serializer.data)

#salva a pontuação
@api_view(['POST'])
def salvar_resultado(request):
    serializer = ResultadoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "Pontuação salva com sucesso!"})
    return Response(serializer.errors, status=400)
