"""durum2 silindi.

Revision ID: 2d3d7fa15c4f
Revises: 82266f0d78ce
Create Date: 2022-01-13 22:44:26.749618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d3d7fa15c4f'
down_revision = '82266f0d78ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('araba', 'durum2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('araba', sa.Column('durum2', sa.BOOLEAN(), nullable=True))
    # ### end Alembic commands ###
