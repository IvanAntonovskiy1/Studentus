import schemdraw
import schemdraw.elements as elm

# Создаем новое изображение схемы
d = schemdraw.Drawing()

# Рисуем компоненты
d += elm.SourceV().up().label('V1', loc='top')
d += elm.Resistor().right().label('R1', loc='top')
d += elm.Capacitor().right().label('C1', loc='top')
d += elm.Line().down().at(d.elements[2].end)
d += elm.Line().left()
d += elm.Line().left()

# Отображаем схему
d.draw()

