class BPMNEditor:  
    """  
    Класс для создания и редактирования BPMN-диаграмм.  

    Attributes:  
        canvas (Canvas): Холст для отрисовки элементов.  
        elements (list): Список элементов диаграммы.  
    """  

    def add_element(self, element_type: str, x: int, y: int) -> None:  
        """  
        Добавляет элемент на холст.  

        Args:  
            element_type (str): Тип элемента (task, gateway, event).  
            x (int): Координата X.  
            y (int): Координата Y.  

        Raises:  
            ValueError: Если элемент не поддерживается.  
        """  
        if element_type not in ["task", "gateway", "event"]:  
            raise ValueError("Недопустимый тип элемента")  
        # ...  