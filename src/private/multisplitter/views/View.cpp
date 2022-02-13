/*
  This file is part of KDDockWidgets.

  SPDX-FileCopyrightText: 2020-2022 Klarälvdalens Datakonsult AB, a KDAB Group company <info@kdab.com>
  Author: Sérgio Martins <sergio.martins@kdab.com>

  SPDX-License-Identifier: GPL-2.0-only OR GPL-3.0-only

  Contact KDAB at <info@kdab.com> for commercial licensing options.
*/

#include "View.h"
#include "../Item_p.h"

using namespace KDDockWidgets;

View::~View()
{
}

void View::free()
{
    delete this;
}

QSize View::sizeHint() const
{
    return {};
}

QSize View::size() const
{
    return geometry().size();
}

QRect View::rect() const
{
    return QRect(QPoint(0, 0), size());
}

int View::x() const
{
    return geometry().x();
}

int View::y() const
{
    return geometry().y();
}

int View::height() const
{
    return geometry().height();
}

int View::width() const
{
    return geometry().width();
}

QSize View::boundedMaxSize(QSize min, QSize max)
{
    // Max should be bigger than min, but not bigger than the hardcoded max
    max = max.boundedTo(Layouting::Item::hardcodedMaximumSize);

    // 0 interpreted as not having max
    if (max.width() <= 0)
        max.setWidth(Layouting::Item::hardcodedMaximumSize.width());
    if (max.height() <= 0)
        max.setHeight(Layouting::Item::hardcodedMaximumSize.height());

    max = max.expandedTo(min);

    return max;
}

/** static */
QSize View::hardcodedMinimumSize()
{
    return Layouting::Item::hardcodedMinimumSize;
}