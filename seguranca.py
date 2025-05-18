import time

class bloqueio_tentativas:
    def __init__(self, tentativas_max = 5, tempo_bloqueio = 60):
        self.tentativas_max = tentativas_max
        self.tempo_bloqueio = tempo_bloqueio
        self.tentativas = {}
        self.bloqueios = {}

    def pode_tentar(self, usuario):
        # Verifica se o usuário está bloqueado
        if usuario in self.bloqueios:
            tempo_passado = time.time() - self.bloqueios[usuario]
            if tempo_passado < self.tempo_bloqueio:
                return False, int(self.tempo_bloqueio - tempo_passado)
            else:
                # desbloqueia
                self.bloqueios.pop(usuario)
                self.tentativas[usuario] = 0
        return True, 0

    def registrar_erro(self, usuario):
        self.tentativas[usuario] = self.tentativas.get(usuario, 0) + 1
        if self.tentativas[usuario] >= self.tentativas_max:
            self.bloqueios[usuario] = time.time()
            return True
        return False

    def resetar_tentativas(self, usuario):
        self.tentativas[usuario] = 0
